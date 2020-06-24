%{?nodejs_find_provides_and_requires}

%global packagename fs-exists-cached

# Tests disabled, as they require a newer npm(tap), but we need this package
# to build a newer npm(tap)
%global enable_tests 0

Name:		nodejs-fs-exists-cached
Version:	1.0.0
Release:	6%{?dist}
Summary:	Just like fs.exists and fs.existsSync, but cached

License:	ISC
URL:		https://github.com/isaacs/fs-exists-cached
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# License file requested at https://github.com/isaacs/fs-exists-cached/issues/1
Source1:	LICENSE-ISC.txt


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	npm(tap)
BuildRequires:	npm(touch)
BuildRequires:	npm(rimraf)
%endif

%description
Just like `fs.exists` and `fs.existsSync`, but cached


%prep
%autosetup -n package
cp -p %{SOURCE1} LICENSE

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/tap test.js --100
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
