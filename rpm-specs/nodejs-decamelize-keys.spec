%{?nodejs_find_provides_and_requires}

%global packagename decamelize-keys

# tests disabled due to missing npm(ava) test suite
%global enable_tests 0

Name:		nodejs-decamelize-keys
Version:	1.1.0
Release:	5%{?dist}
Summary:	Convert object keys from camelCase to lowercase with a custom separator

License:	MIT
URL:		https://github.com/dsblv/decamelize-keys.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/dsblv/decamelize-keys/v%{version}/test.js


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

BuildRequires:	npm(decamelize)
BuildRequires:	npm(map-obj)
%if 0%{?enable_tests}
BuildRequires:	npm(ava)
%endif

%description
Convert object keys from camelCase to lowercase with a custom separator


%prep
%autosetup -n package
cp -p %{SOURCE1} .

%nodejs_fixdep map-obj '^2.0.0'

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/ava -v
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license license
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 27 2018 jsmith <jsmith.fedora@gmail.com> - 1.1.0-1
- Initial packaging
