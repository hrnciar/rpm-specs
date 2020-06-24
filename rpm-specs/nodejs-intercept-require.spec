%{?nodejs_find_provides_and_requires}

%global packagename intercept-require

# tests disabled because the tests assume they're being run in a directory
# named 'intercept-require', even though the tarball creates a directory called
# 'package'
%global enable_tests 0

Name:		nodejs-intercept-require
Version:	1.1.0
Release:	5%{?dist}
Summary:	Intercept calls to require()

License:	MIT
URL:		https://github.com/nickb1080/intercept-require.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


BuildArch:	noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(callsite)
BuildRequires:	npm(object-assign)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(expect)
%endif

%description
Intercept calls to require()


%prep
%setup -q -n package 

%nodejs_fixdep object-assign

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec test/test.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
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

* Tue Apr 24 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Initial packaging
