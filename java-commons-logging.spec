Summary:	Jakarta Commons Logging - interface for logging systems
Summary(pl):	Jakarta Commons Logging - interfejs do systemów loguj±cych
Name:		jakarta-commons-logging
Version:	1.0.4
Release:	2
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/logging/source/commons-logging-%{version}-src.tar.gz
# Source0-md5:	db5dc75c89e794f794be92d10df6be1b
URL:		http://jakarta.apache.org/commons/logging/
BuildRequires:	ant
BuildRequires:	jdk >= 1.4
BuildRequires:	jpackage-utils
BuildRequires:	logging-log4j
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

%description -l pl
Pakiet commons-logging dostarcza prostego, zorientowanego na
komponenty interfejsu (org.apache.commons.logging.Log) wraz z
wrapperami do systemów loguj±cych. U¿ytkownik mo¿e wybraæ w czasie
uruchamiania, którego systemu chce u¿ywaæ. Ponadto dostarczona jest
niewielka liczba podstawowych implementacji, aby pozwoliæ u¿ytkownikom
na u¿ywanie pakietu samodzielnie.

%package javadoc
Summary:	Jakarta Commons Logging documentation
Summary(pl):	Dokumentacja do Jakarta Commons Logging
Group:		Development/Languages/Java
Requires:	jpackage-utils
Obsoletes:	jakarta-commons-logging-doc

%description javadoc
Jakarta Commons Logging documentation.

%description javadoc -l pl
Dokumentacja do Jakarta Commons Logging.

%prep
%setup -q -n commons-logging-%{version}-src

%build
export CLASSPATH="`build-classpath log4j`"
export JAVA_HOME="%{java_home}"
%ant dist javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}

install dist/commons-logging-api.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}-api.jar
install dist/commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-%{version}.jar
ln -s commons-logging-%{version}-api.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging-api.jar
ln -s commons-logging-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/commons-logging.jar

cp -R dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/*.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
