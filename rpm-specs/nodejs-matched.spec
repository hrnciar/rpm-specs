%{?nodejs_find_provides_and_requires}

%global packagename matched

%global enable_tests 1

Name:		nodejs-matched
Version:	1.0.2
Release:	8%{?dist}
Summary:	Adds array support to node-glob, sync and async

License:	MIT
URL:		https://github.com/jonschlinkert/matched
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source{1-9} are generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source10:	dl-tests.sh


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(arr-union)
BuildRequires:	npm(lazy-cache)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(chai)
BuildRequires:	npm(arr-union)
BuildRequires:	npm(async-array-reduce)
BuildRequires:	npm(bluebird)
BuildRequires:	npm(chai)
BuildRequires:	npm(extend-shallow)
BuildRequires:	npm(fs-exists-sync)
BuildRequires:	npm(glob)
BuildRequires:	npm(has-glob)
BuildRequires:	npm(is-valid-glob)
BuildRequires:	npm(resolve-dir)
BuildRequires:	npm(rimraf)
%endif

%description
Adds array support to node-glob, sync and async. Also supports tilde expansion
(user home) and resolving to global npm modules.


%prep
%autosetup -n package
# setup the tests
%autosetup -T -D -a 1 -n package

%nodejs_fixdep async-array-reduce '^0.2.0'
%nodejs_fixdep glob
%nodejs_fixdep resolve-dir

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Update to upstream 1.0.2 release

* Tue Apr 18 2017 Jared Smith <jsmith@fedoraproject.org> - 0.4.4-2
- Relax dependency on npm(resolve-dir)

* Sat Apr 15 2017 Jared Smith <jsmith@fedoraproject.org> - 0.4.4-1
- Update to upstream 0.4.4 release

* Tue Aug 09 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.3-3
- Relax dependency on npm(async-array-reduce)

* Fri Jul 29 2016 Jared Smith <jsmith@fedoraproject.org>
- Relax dependency on npm(glob)

* Fri Jul 29 2016 Jared Smith <jsmith@fedoraproject.org>
- new version

* Fri Jul 29 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.3-1
- Initial packaging
