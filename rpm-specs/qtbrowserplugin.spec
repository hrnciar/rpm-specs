%global commit 80592b0e7145fb876ea0e84a6e3dadfd5f7481b6

Name:           qtbrowserplugin
Version:        2.4
Release:        15%{?dist}
Summary:        Qt Solutions Component: Browser Plugin

License:        BSD
URL:            http://qt.gitorious.org/qt-solutions/qt-solutions
# git archive --prefix=qtbrowserplugin-2.4/ 80592b0e7145fb876ea0e84a6e3dadfd5f7481b6:qtbrowserplugin/ | gzip > ../qtbrowserplugin-2.4-80592b0e7145fb876ea0e84a6e3dadfd5f7481b6.tar.gz
Source0:        qtbrowserplugin-%{version}-%{commit}.tar.gz
# Patch to build as a library
Patch0:         qtbrowserplugin-lib.patch

BuildRequires:  qt-devel

# -debuginfo useless for (only) static libs
%global debug_package   %{nil}

%description
The QtBrowserPlugin solution is useful for implementing plugins
for web browser.


%package        devel
Summary:        Development files for %{name}
Requires:       qt-devel%{?_isa}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The QtBrowserPlugin solution is useful for implementing plugins
for web browser.


%prep
%setup -q
%patch0 -p1 -b .lib


%build
%{qmake_qt4}
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}
cp -p libqtbrowserplugin.* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
cp -p src/*.h %{buildroot}%{_includedir}


%files devel
%doc doc examples README.TXT
%{_includedir}/*
%{_libdir}/lib%{name}.a


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.4-6
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 5 2013 Orion Poplawski <orion@cora.nwra.com> - 2.4-2
- Use explicit name for library file

* Thu Sep 5 2013 Orion Poplawski <orion@cora.nwra.com> - 2.4-1
- Initial Fedora package
