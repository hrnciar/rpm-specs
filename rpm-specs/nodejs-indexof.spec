%{?nodejs_find_provides_and_requires}

%global packagename indexof
%global enable_tests 1

Name: nodejs-%{packagename}
Version: 0.0.1
Release: 9%{?dist}
Summary: Lame indexOf thing
    
License: MIT
URL: https://www.npmjs.com/package/indexof
Source0: http://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires: nodejs

%description
%{summary}.

%prep
%autosetup -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%{__nodejs} -e 'require("./")'
%endif

%files
%doc Readme.md
%{nodejs_sitelib}/%{packagename}


%changelog
* Thu Aug 06 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-9
- Fixes FTBFS
- Use BR nodejs instead of nodejs-packaging

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.0.1-1
- First release 
