%{?nodejs_find_provides_and_requires}

%global packagename global-modules
%global enable_tests 1

# Bootstrap mode, because resolve-dir has a build-time dependency on
# global-modules, and global-modules has a run-time dependency on resolve-dir
#
# So, in bootstrap mode, we remove the run-time dependency on resolve-dir so
# that we can actually build resolve-dir
%global bootstrap 0

Name:		nodejs-global-modules
Version:	1.0.0
Release:	10%{?dist}
Summary:	The directory used by npm for globally installed npm modules

License:	MIT
URL:		https://github.com/jonschlinkert/global-modules.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/global-modules/%{version}/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(global-prefix)
BuildRequires:	npm(is-windows)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(fs-exists-sync)
BuildRequires:	npm(global-prefix)
BuildRequires:	npm(is-windows)
%endif

%description
The directory used by npm for globally installed npm modules.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .

%if 0%{?bootstrap}
%nodejs_fixdep -r resolve-dir
%endif

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
NODE_ENV=test %{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-3
- Turn off bootstrap mode, now that npm(resolve-dir) is built

* Thu Sep 21 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Turn on bootstrap mode to be able to build npm(resolve-dir)

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Update to upstream 1.0.0 release

* Sun Apr 16 2017 Jared Smith <jsmith@fedoraproject.org> - 0.2.3-1
- Update to upstream 0.2.3 release

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.2.2-1
- Initial packaging
