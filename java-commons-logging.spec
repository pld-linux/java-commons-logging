# NOTE:
# - when upgrading, please sync Source100 and Patch100 in tomcat.spec
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%define		srcname	commons-logging
Summary:	Commons Logging - interface for logging systems
Summary(pl.UTF-8):	Commons Logging - interfejs do systemów logujących
Name:		java-commons-logging
Version:	1.1.3
Release:	1
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/logging/source/commons-logging-%{version}-src.tar.gz
# Source0-md5:	e8e197d628436490886d17cffa108fe3
Patch0:		build.xml.patch
URL:		http://commons.apache.org/logging/
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	java(servlet)
BuildRequires:	java-avalon-framework
BuildRequires:	java-avalon-logkit
BuildRequires:	java-junit
BuildRequires:	java-log4j
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
Requires:	jre >= 1.4
Obsoletes:	jakarta-commons-logging
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.

%description -l pl.UTF-8
Pakiet commons-logging dostarcza prostego, zorientowanego na
komponenty interfejsu (org.apache.commons.logging.Log) wraz z
wrapperami do systemów logujących. Użytkownik może wybrać w czasie
uruchamiania, którego systemu chce używać. Ponadto dostarczona jest
niewielka liczba podstawowych implementacji, aby pozwolić użytkownikom
na używanie pakietu samodzielnie.

%prep
%setup -q -n commons-logging-%{version}-src

%undos build.xml
%patch0 -p1

%build
cat > build.properties << EOF
log4j12.jar=%(find-jar log4j)
junit.jar=%(find-jar junit)
logkit.jar=%(find-jar avalon-logkit)
avalon-framework-impl.jar=%(find-jar avalon-framework-impl.jar)
avalon-framework-api.jar=%(find-jar avalon-framework-api.jar)
servletapi.jar=%(find-jar servlet-api.jar)
EOF

! grep -q '=$' build.properties

export LC_ALL=en_US

# like default but without test
%ant clean compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install target/commons-logging-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}.jar
install target/commons-logging-adapters-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-adapters-%{version}.jar
install target/commons-logging-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-api-%{version}.jar

ln -s commons-logging-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging.jar
ln -s commons-logging-adapters-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-adapters.jar
ln -s commons-logging-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-api.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE.txt PROPOSAL.html RELEASE-NOTES.txt license-header.txt
%{_javadir}/commons-logging-%{version}.jar
%{_javadir}/commons-logging.jar
%{_javadir}/commons-logging-adapters-%{version}.jar
%{_javadir}/commons-logging-adapters.jar
%{_javadir}/commons-logging-api-%{version}.jar
%{_javadir}/commons-logging-api.jar
