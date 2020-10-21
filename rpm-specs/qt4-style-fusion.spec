%global snap hg20151214

Name:           qt4-style-fusion
Version:        0
Release:        11.%{snap}%{?dist}
Summary:        Fusion widget style for Qt4

License:        LGPLv2
URL:            https://code.google.com/p/fusion-qt4/
# hg clone https://code.google.com/p/fusion-qt4/ qt4-style-fusion
# find qt4-style-fusion -name ".hg" -exec rm -rf {} \;
# tar cJf qt4-style-fusion-hg$(date +%%Y%%m%%d).tar.xz qt4-style-fusion
Source0:        %{name}-%{snap}.tar.xz
# Taken from Qt4 sources
Source1:        qstylehelper.cpp

# Fix build scripts
Patch0:         fusion-qt4_build.patch

BuildRequires:  gcc-c++
BuildRequires:  qt4-devel-private

%{?_qt4_version:Requires: qt4%{?_isa} = %{_qt4_version}}


%description
Qt4 backport of the Qt5 fusion widget style.


%prep
%setup -q -n %{name}
%patch0 -p1
cp -a %{SOURCE1} .


%build
%qmake_qt4 .
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}


%files
%{_qt4_plugindir}/styles/libfusion.so


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.hg20151214
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Sandro Mani <manisandro@gmail.com> - 0-1.hg20151112
- Initial package
