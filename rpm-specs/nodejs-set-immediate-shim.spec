# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

# tests disabled due to circular dep, can be enabled later
%global enable_tests 0
%global srcname set-immediate-shim

Name:           nodejs-%{srcname}
Version:        1.0.1
Release:        11%{?dist}
Summary:        Simple setImmediate shim
License:        MIT
URL:            https://github.com/sindresorhus/set-immediate-shim
Source0:        https://github.com/sindresorhus/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
BuildRequires:  npm(require-uncached)
%endif


%description
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}
rm -rf node_modules/


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
node test.js
%endif


%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{srcname}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 27 2016 Tom Hughes <tom@compton.nu> - 1.0.1-4
- Update source to actually be 1.0.1 not 1.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sun Mar  8 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-2
- Update Source0 to comply with github source guidelines
- Move license from %%doc to %%license

* Wed Dec 31 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.0.0-1
- Initial package
