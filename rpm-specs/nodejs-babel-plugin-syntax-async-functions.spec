%{?nodejs_find_provides_and_requires}

%global packagename babel-plugin-syntax-async-functions
%global enable_tests 1

Name:		nodejs-babel-plugin-syntax-async-functions
Version:	6.13.0
Release:	5%{?dist}
Summary:	Allow parsing of async functions

License:	MIT
URL:		https://github.com/babel/babel/tree/v%{version}/packages/babel-plugin-syntax-async-functions
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# license
Source1:	https://raw.githubusercontent.com/babel/babel/v%{version}/LICENSE


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging

%if 0%{?enable_tests}
#BuildRequires:	
%endif

%description
Allow parsing of async functions


%prep
%autosetup -n package
cp -p %{SOURCE1} .


%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[103m -=#=- This module has no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Jared K. Smith <jsmith@fedoraproject.org> - 6.13.0-1
- Initial packaging
