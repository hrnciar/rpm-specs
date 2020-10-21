%{?nodejs_find_provides_and_requires}

%global packagename glob-expand
%global enable_tests 1

Name:		nodejs-glob-expand
Version:	0.2.1
Release:	7%{?dist}
Summary:	A sync glob / minimatch / RegExp function

License:	MIT
URL:		https://github.com/anodynos/node-glob-expand
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	source-%{version}.tar.bz2
Source10:	dl-tests.sh


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	coffee-script
BuildRequires:	npm(glob)
BuildRequires:	npm(lodash)

%if 0%{?enable_tests}
# nothing
%endif

%description
A sync glob / minimatch / RegExp function with a gruntjs-like *expand* of
patterns, with minimum dependencies. Derived from gruntjs's v0.4.1
file.expand.


%prep
%autosetup -n package
# setup the sources
%setup -q -T -D -a 1 -n package

rm -rf build/code/*.js

%nodejs_fixdep glob
%nodejs_fixdep lodash

%build
%nodejs_symlink_deps --build
# Building with straight coffeescript instead of using uRequire
# but it should work fine
coffee -o build/code/ -bc source/code/*.coffee
rm -rf node_modules

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json build/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/echo -e "\e[101m -=#=- This package has no tests -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.1-1
- Update to upstream 0.2.1 release

* Fri Jul 29 2016 Jared Smith <jsmith@fedoraproject.org> - 0.2.0-1
- Initial packaging
