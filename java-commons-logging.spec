%include	/usr/lib/rpm/macros.java
Summary:	Commons Logging - interface for logging systems
Summary(pl.UTF-8):	Commons Logging - interfejs do systemów logujących
Name:		java-commons-logging
Version:	1.1.1
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/commons/logging/source/commons-logging-%{version}-src.tar.gz
# Source0-md5:	e5cfa8cca13152d7545fde6b1783c60a
Patch0:		%{name}-target.patch
URL:		http://commons.apache.org/logging/
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	avalon-framework
BuildRequires:	avalon-logkit
BuildRequires:	jakarta-servletapi >= 4
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	logging-log4j
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre >= 1.4
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
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
Commons Logging documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do Commons Logging.

%prep
%setup -q -n commons-logging-%{version}-src
#%patch0 -p1

%build
required_jars="log4j junit avalon-logkit avalon-framework-impl servlet-api"
export CLASSPATH=$(build-classpath $required_jars)
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

install dist/commons-logging-api.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}-api.jar
install dist/commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}.jar
ln -s commons-logging-%{version}-api.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-api.jar
ln -s commons-logging-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging.jar

cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
