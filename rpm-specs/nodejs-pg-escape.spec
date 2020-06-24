%{?nodejs_find_provides_and_requires}

Name:           nodejs-pg-escape
Version:        0.2.0
Release:        10%{?dist}
Summary:        Escape postgres queries which do not support stored procedures

License:        MIT
URL:            https://www.npmjs.com/package/pg-escape
Source0:        https://registry.npmjs.org/pg-escape/-/pg-escape-%{version}.tgz
# https://github.com/segmentio/pg-escape/pull/14
Source1:        nodejs-pg-escape-license.txt
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)
BuildRequires:  npm(should)


%description
%{summary}.


%prep
%autosetup -n package
cp %{SOURCE1} LICENSE
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -p reserved.txt %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}%{nodejs_sitelib}/pg-escape
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/pg-escape
ln -s %{_datadir}/%{name}/reserved.txt %{buildroot}%{nodejs_sitelib}/pg-escape
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --require should --reporter spec


%files
%{!?_licensedir:%global license %doc}
%doc Readme.md History.md
%license LICENSE
%{nodejs_sitelib}/pg-escape
%{_datadir}/%{name}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec  5 2015 Tom Hughes <tom@compton.nu> - 0.2.0-2
- Own the data directory

* Thu Dec  3 2015 Tom Hughes <tom@compton.nu> - 0.2.0-1
- Initial build of 0.2.0
