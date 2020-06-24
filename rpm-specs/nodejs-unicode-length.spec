%{?nodejs_find_provides_and_requires}

%global packagename unicode-length
%global enable_tests 1
%global commit ac7ec6e3dc1278d1cfdcd7a3bfcd66db0a4f131e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		nodejs-unicode-length
Version:	1.0.2
Release:	8%{?dist}
Summary:	Get the length of unicode strings

License:	MIT
URL:		https://github.com/jviotti/unicode-length.git
#Source0:        https://github.com/jviotti/unicode-length/archive/v%{version}/unicode-length-%{version}.tar.gz
Source0:    https://github.com/jviotti/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	coffee-script

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(chai)
BuildRequires:	npm(lodash)
BuildRequires:	npm(chalk)
%endif

%description
Get the length of unicode strings


%prep
%autosetup -n %{packagename}-%{commit}

# remove the pre-build version
rm build/unicode-length.js

# This package says it depends on chalk "^1.0.0", but there aren't
# any API changes between 0.4.0 and 1.0.0 (see upstream issue at
# https://github.com/chalk/chalk/issues/44). Bringing the chalk package up to
# 1.0.0 in Fedora would be a lot of extra work, so in the name of efficiency
# I'm going to roll this back and allow any version of chalk
%nodejs_fixdep chalk

%build
# compile the .js file from the coffee-script version
coffee -c -b -o build/ lib/*.coffee
# copy the build .js file to lib/, for the tests
cp build/*.js lib/

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json build %{buildroot}%{nodejs_sitelib}/%{packagename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
# Compile the tests from coffee-script to js
coffee -c -b tests/*.coffee
%{_bindir}/mocha -R spec tests
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 18 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Update to 1.0.2, fix punycode 2.0.0

* Thu Jul 28 2016 Tom Hughes <tom@compton.nu> - 1.0.1-1
- Update to 1.0.1 upstream release
- Relax npm(punycode) dependency for Node.js 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-6
- Fix dependency on npm(chalk) version

* Sat Nov 07 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-5
- Add missing BuildRequire for mocha

* Fri Nov 06 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-4
- Fix tests
- Fix inclusion of build directory
- Rebuild the .js from the source .coffee files

* Wed Oct 28 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
