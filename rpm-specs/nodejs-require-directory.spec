%global commit cc71c23dd0c16cefd26855303c16ca1b9b50a36d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           nodejs-require-directory
Version:        2.1.1
Release:        10%{?dist}
Summary:        Recursively iterates over specified directory, require()'ing each file

License:        MIT
URL:            https://github.com/troygoode/node-require-directory
Source0:        https://github.com/troygoode/node-require-directory/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(mocha)


%description
%{summary}.


%prep
%autosetup -n node-require-directory-%{commit}
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/require-directory
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/require-directory
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
mocha


%files
%doc README.markdown
%license LICENSE
%{nodejs_sitelib}/require-directory


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Tom Hughes <tom@compton.nu> - 2.1.1-8
- Resurrect retired package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.1.1-1
- Initial package
