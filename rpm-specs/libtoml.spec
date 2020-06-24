%global libname toml

%global commit 03e8a3ab1d4d014e63a2befe8a48e74783a81521
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           lib%{libname}
Version:        0
Release:        15.20161213git%{shortcommit}%{?dist}
Summary:        Fast C parser using Ragel to generate the state machine.

License:        BSD
URL:            https://github.com/ajwans/libtoml
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# https://github.com/ajwans/libtoml/pull/15
Patch0001:      0001-add-meson-buildsystem-as-experiment.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  %{_bindir}/ragel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(cunit)

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/%{libname}
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{libname}.h
%{_libdir}/%{name}.so

%changelog
* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 0-15.20161213git03e8a3a
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0-13.20161213git03e8a3a
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-12.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-11.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0-10.20161213git03e8a3a
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0-8.20161213git03e8a3a
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0-7.20161213git03e8a3a
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-6.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0-5.20161213git03e8a3a
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-2.20161213git03e8a3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-1.20161213git03e8a3a
- Initial package
