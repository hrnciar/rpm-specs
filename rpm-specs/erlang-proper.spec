%global realname proper
%global upstream proper-testing


Name:       erlang-%{realname}
Version:    1.3
Release:    5%{?dist}
BuildArch:  noarch
License:    GPLv3+
Summary:    A QuickCheck-inspired property-based testing tool for Erlang
URL:        https://github.com/%{upstream}/%{realname}
VCS:        scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:    https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:     erlang-proper-0001-Disable-one-test-case.patch
BuildRequires: erlang-rebar


%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
# The docs need to be built first: https://github.com/proper-testing/proper/issues/179
./make_doc
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license COPYING
%doc doc
%doc examples
%doc README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.3-4
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.3-1
- Update to 1.3 (#1608383).
- https://github.com/proper-testing/proper/releases/tag/v1.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2-8
- Convert into a noarch package.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 25 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2-4
- Apply a patch from upstream that allows the slow arches to pass all tests.

* Sun Feb 19 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.2-3
- Skip a test on slow arches, as it is too slow and times out (#1423535).
- Replace some tabs with spaces.
- Reorganize the spec file a bit.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
