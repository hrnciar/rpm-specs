%global shortname doctrine

Name:           nodejs-doctrine
Version:        0.6.4
Release:        10%{?dist}
Summary:        A JSDoc parser

# README.md states that some functions are 'derived' from esprima (BSD) and
# some 'extensions' are 'derived' from closure-compiler (ASL 2.0)
License:        BSD and ASL 2.0

URL:            https://github.com/Constellation/%{shortname}
Source0:        http://registry.npmjs.org/%{shortname}/-/%{shortname}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(should)
BuildRequires:  npm(esutils)
BuildRequires:  npm(isarray)

%description
%{shortname} is %{summary}.

%prep
%setup -qn package
%nodejs_fixdep esutils

%build
# Nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{shortname}/
cp -pr package.json lib/ %{buildroot}%{nodejs_sitelib}/%{shortname}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check

# Test dep 'describe' is not packaged for Fedora yet
for test in $(ls test/ | grep -v {midstream,parse}.js); do
    node test/${test}
done

%files
%{nodejs_sitelib}/%{shortname}
%doc README.md CONTRIBUTING.md
# LICENSE.BSD and LICENSE.esprima are identical, so only one is included
%license LICENSE.BSD LICENSE.closure-compiler


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 07 2015 Gerard Ryan <galileo@fedoraproject.org> - 0.6.4-1
- Initial package
