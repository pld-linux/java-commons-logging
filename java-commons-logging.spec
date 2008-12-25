# TODO
# - update to 1.1 from DEVEL
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%include	/usr/lib/rpm/macros.java
Summary:	Jakarta Commons Logging - interface for logging systems
Summary(pl.UTF-8):	Jakarta Commons Logging - interfejs do systemów logujących
Name:		java-commons-logging
Version:	1.0.4
Release:	4
License:	Apache
Group:		Libraries/Java
Source0:	http://archive.apache.org/dist/commons/logging/source/commons-logging-%{version}-src.tar.gz
# Source0-md5:	db5dc75c89e794f794be92d10df6be1b
Patch0:		jakarta-commons-logging-target.patch
URL:		http://commons.apache.org/logging/
BuildRequires:	ant
BuildRequires:	avalon-framework-api
BuildRequires:	avalon-logkit
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	logging-log4j
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre >= 1.4
Provides:	jakarta-commons-logging
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

%package javadoc
Summary:	Jakarta Commons Logging documentation
Summary(pl.UTF-8):	Dokumentacja do Jakarta Commons Logging
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-logging-doc

%description javadoc
Jakarta Commons Logging documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Jakarta Commons Logging.

%prep
%setup -q -n commons-logging-%{version}-src
%patch0 -p1

%build
required_jars="log4j junit avalon-logkit avalon-framework-api"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a dist/commons-logging-api.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}-api.jar
cp -a dist/commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}.jar
ln -s commons-logging-%{version}-api.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-api.jar
ln -s commons-logging-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif
