Summary:	Jakarta Commons Logging
Name:		jakarta-commons-logging
Version:	1.0.2
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/jakarta-commons/release/commons-logging/v%{version}/commons-logging-%{version}-src.tar.gz
URL:		http://jakarta.apache.org/
Requires:	jre
BuildRequires:	jakarta-ant
BuildRequires:	jakarta-log4j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Jakarta Commons Logging.

%package doc
Summary:	Jakarta Commons Logging
Group:		Development/Languages/Java

%description doc
Jakarta Commons Logging.

%prep
%setup -q -n commons-logging-%{version}-src

%build
touch LICENSE
cd logging
ant dist

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install logging/dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc logging/dist/LICENSE
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc logging/dist/docs
