Summary:	Jakarta Commons Logging - interface for logging systems
Summary(pl):	Jakarta Commons Logging - interfejs do systemów loguj±cych
Name:		jakarta-commons-logging
Version:	1.0.3
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/jakarta/commons/logging/source/commons-logging-%{version}-src.tar.gz
# Source0-md5:	d40606211a1559a9d9fd35eb9091ac15
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	jakarta-log4j
BuildRequires:	jdk >= 1.4
Requires:	jre >= 1.4
BuildArch:	noarch
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

%package doc
Summary:	Jakarta Commons Logging documentation
Summary(pl):	Dokumentacja do Jakarta Commons Logging
Group:		Development/Languages/Java

%description doc
Jakarta Commons Logging documentation.

%description doc -l pl
Dokumentacja do Jakarta Commons Logging.

%prep
%setup -q -n commons-logging-%{version}-src

%build
cat << EOF > build.properties
log4j.jar=%{_javadir}/log4j.jar
EOF
ant \
    -Dlog4j.jar=%{_javadir}/log4j.jar \
    dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/LICENSE.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc dist/docs
