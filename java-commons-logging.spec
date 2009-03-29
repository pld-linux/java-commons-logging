%bcond_with	java_sun	# build with java-sun

%if "%{pld_release}" == "ti"
%define	with_java_sun	1
%endif

%define		srcname	commons-logging

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
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	jpackage-utils
BuildRequires:	junit
BuildRequires:	logging-log4j
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre >= 1.4
Obsoletes:	jakarta-commons-logging
Provides:	jakarta-commons-logging
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
Summary:	Commons Logging documentation
Summary(pl.UTF-8):	Dokumentacja do Commons Logging
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-logging-doc
Obsoletes:	jakarta-commons-logging-javadoc

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
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{srcname}-%{version}}

install dist/%{srcname}-api.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}-api.jar
install dist/%{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}-api.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-api.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

cp -a dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
