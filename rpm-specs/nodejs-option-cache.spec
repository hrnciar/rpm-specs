%{?nodejs_find_provides_and_requires}

%global packagename option-cache
%global enable_tests 1

Name:		nodejs-option-cache
Version:	4.0.0
Release:	6%{?dist}
Summary:	Simple API for managing options in JavaScript applications

License:	MIT
URL:		https://github.com/jonschlinkert/option-cache
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(lazy-cache)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(arr-flatten)
BuildRequires:	npm(collection-visit)
BuildRequires:	npm(component-emitter)
BuildRequires:	npm(get-value)
BuildRequires:	npm(has-value)
BuildRequires:	npm(kind-of)
BuildRequires:	npm(set-value)
BuildRequires:	npm(should)
BuildRequires:	npm(to-object-path)
%endif

%description
Simple API for managing options in JavaScript applications.


%prep
%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package

%nodejs_fixdep collection-visit
%nodejs_fixdep set-value

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js utils.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
ln -sf %{nodejs_sitelib}/should node_modules/should
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Jared Smith <jsmith@fedoraproject.org> - 4.0.0-1
- Update to upstream 4.0.0 release

* Sat Apr 15 2017 Jared Smith <jsmith@fedoraproject.org> - 3.4.0-2
- Relax version of npm(collection-visit) and npm(set-value)

* Sat Apr 15 2017 Jared Smith <jsmith@fedoraproject.org> - 3.4.0-1
- Initial packaging
