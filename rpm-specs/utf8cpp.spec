# This package only contains header files.
%global debug_package %{nil}

Name:       utf8cpp
Version:    3.1
Release:    2%{?dist}
Summary:    A simple, portable and lightweight library for handling UTF-8 encoded strings
License:    Boost
URL:        https://github.com/nemtrif/utfcpp
Source0:    https://github.com/nemtrif/utfcpp/archive/v%{version}/utfcpp-%{version}.tar.gz
Patch0:     %{name}-use-system-gtest.patch
# put cmake import file in arch-agnostic directory
Patch1:     %{name}-noarch.patch
BuildRequires: cmake3
BuildRequires: gcc-c++
BuildRequires: gtest-devel

%description
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.

%package    devel
Summary:    Header files for %{name}
BuildArch:  noarch
Provides:   %{name}-static = %{version}-%{release}
Requires:   cmake-filesystem

%description devel
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.

%prep
%setup -q -n utfcpp-%{version}
%patch0 -p1 -b .gtest
%patch1 -p1 -b .noarch
#%%patch10 -p1
mkdir build

%build
pushd build
%cmake3 \
   -DUTF8_TESTS=ON \
   -DUTF8_SAMPLES=ON \
   ..
%make_build
popd

%install
pushd build
%make_install
popd
pushd %{buildroot}%{_includedir}
ln -s utf8cpp/utf8.h ./
mkdir utf8
for f in {{un,}checked,core,cpp11}.h ; do
    ln -s ../utf8cpp/utf8/${f} utf8/
done
popd

%check
pushd build
%make_build test
popd

%files devel
%doc README.md samples/docsample.cpp
%{_includedir}/utf8.h
%dir %{_includedir}/utf8
%{_includedir}/utf8/checked.h
%{_includedir}/utf8/core.h
%{_includedir}/utf8/cpp11.h
%{_includedir}/utf8/unchecked.h
%{_includedir}/utf8cpp
%{_datadir}/cmake/utf8cpp

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 3.1-1
- update to 3.1
- include cmake import file
- symlink headers in the previous location for compatibility

* Mon Oct 21 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2.3.6-1
- update to 2.3.6
- new upstream location
- use cmake and run tests
- switch main package to archful per
  https://docs.fedoraproject.org/en-US/packaging-guidelines/#_do_not_use_noarch

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-4
- fix docs macro

* Wed Apr 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-3
- drop base package

* Wed Apr 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-2
- add Provides: utf8cpp-static
- fix Source0 URL
- add missing BuildArch: noarch

* Sat Mar 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-1
- initial package
