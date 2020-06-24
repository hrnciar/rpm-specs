%{?nodejs_find_provides_and_requires}

%global packagename parse-glob
# tests disabled due to npm(is-glob) >= 4.0.0
%global enable_tests 0

Name:		nodejs-parse-glob
Version:	3.0.4
Release:	9%{?dist}
Summary:	Parse a glob pattern into an object of tokens

License:	MIT
URL:		https://github.com/jonschlinkert/parse-glob.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:	https://raw.githubusercontent.com/jonschlinkert/parse-glob/%{version}/test.js


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(glob-base)
BuildRequires:	npm(is-dotfile)
BuildRequires:	npm(lodash)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
%endif

%description
Parse a glob pattern into an object of tokens.


%prep
%setup -q -n package
# setup the tests
cp -p %{SOURCE1} .

%nodejs_fixdep is-extglob
%nodejs_fixdep is-glob

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
ln -s %{nodejs_sitelib}/should node_modules/should
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.4-4
- Relax dependency on npm(is-glob)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 3.0.4-2
- Relax dependency on npm(is-extglob)

* Tue Feb  9 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.4-1
- Initial packaging
