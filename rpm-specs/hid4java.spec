Name: hid4java
Version: 0.5.0
Release: 5%{?dist}
Summary: Java wrapper for the hidapi library

License: MIT
URL: http://github.com/gary-rowe/hid4java
Source0: https://github.com/gary-rowe/%{name}/archive/%{name}-%{version}.tar.gz
Patch0: load-system-hidapi-usb-library.patch
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(net.java.dev.jna:jna)

Requires: hidapi

%description
hid4java supports USB HID devices through a common API. The API is very simple
but provides great flexibility such as support for feature reports and blocking
reads with timeouts. Attach/detach events are provided to allow applications to
respond instantly to device availability.


%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.dll' -print -delete

%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc AUTHORS README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Jonny Heggheim <hegjon@gmail.com> - 0.5.0-1
- Update to version 0.5.0

* Mon Jul 09 2018 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-7
- Fixed FTBFS (bug #1555877)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-2
- Fixed the dependency for hidapi

* Mon Aug 24 2015 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-1
- Update to upstream version 0.4.0

* Fri Aug 07 2015 Jonny Heggheim <hegjon@gmail.com> - 0.4.0-0.1.gitb010cee
- Inital packaging
