%{?nodejs_find_provides_and_requires}

%global packagename resolve-dir
%global enable_tests 1

Name:		nodejs-resolve-dir
Version:	1.0.1
Release:	6%{?dist}
Summary:	Resolve a directory

License:	MIT
URL:		https://github.com/jonschlinkert/resolve-dir.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# The 0.1.0 release hasn't been tagged in Github, so pull test from master for now
Source1:	https://raw.githubusercontent.com/jonschlinkert/resolve-dir/master/test.js



BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(expand-tilde)
BuildRequires:	npm(global-modules)

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(user-home)
%endif

%description
Resolve a directory that is either local, global or in the user's home
directory.


%prep
%autosetup -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep expand-tilde

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
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Update to upstream 1.0.1 release

* Sun Apr 16 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Allow newer npm(expand-tilde)

* Sat Apr 15 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Update to upstream 1.0.0 release

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-1
- Initial packaging
