%{?nodejs_find_provides_and_requires}

Name:           nodejs-foreach
Version:        2.0.5
Release:        10%{?dist}
Summary:        Iterate over the key value pairs of an object

License:        MIT
URL:            https://github.com/manuelstofer/foreach
Source0:        https://registry.npmjs.org/foreach/-/foreach-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tape)


%description
Iterate over the key value pairs of either an array-like
object or a dictionary like object.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/foreach
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/foreach
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} test.js


%files
%{!?_licensedir:%global license %doc}
%doc Readme.md
%license LICENSE
%{nodejs_sitelib}/foreach


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 26 2015 Tom Hughes <tom@compton.nu> - 2.0.5-2
- Shorten summary

* Thu Oct 22 2015 Tom Hughes <tom@compton.nu> - 2.0.5-1
- Initial build of 2.0.5
