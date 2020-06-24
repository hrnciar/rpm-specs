%{?nodejs_find_provides_and_requires}

%global packagename safe-regex
%global enable_tests 1

Name:		nodejs-safe-regex
Version:	1.1.0
Release:	5%{?dist}
Summary:	Detect possibly catastrophic, exponential-time regular expressions

License:	MIT
URL:		https://github.com/substack/safe-regex.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(ret)

%if 0%{?enable_tests}
BuildRequires:	npm(tape)
%endif

%description
Detect possibly catastrophic, exponential-time regular expressions.


%prep
%autosetup -n package

%nodejs_fixdep ret '^0.2.2'

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/tape test/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.markdown
%license LICENSE
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

* Fri Apr 20 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Initial packaging
