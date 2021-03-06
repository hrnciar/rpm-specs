%{?nodejs_find_provides_and_requires}

%global packagename svgo

# Several tests are currently failing for an unknown reason
%global enable_tests 0

Name:		nodejs-svgo
Version:	0.7.2
Release:	9%{?dist}
Summary:	Nodejs-based tool for optimizing SVG vector graphics files

License:	MIT
URL:		https://github.com/svg/svgo.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:	tests-%{version}.tar.bz2
Source2:	docs-%{version}.tar.bz2
Source3:	examples-%{version}.tar.bz2
Source10:	dl-tests.sh

# For some reason, the test suite doesn't like underscores in the entity names
# So I simply removed them with this patch.
Patch0:		nodejs-svgo_fix-entity-underscores.patch


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(sax)
BuildRequires:	npm(whet.extend)
BuildRequires:	npm(js-yaml)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(csso)
BuildRequires:	npm(should)
%endif

Requires:	nodejs

%description
Nodejs-based tool for optimizing SVG vector graphics files


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package
%setup -q -T -D -a 2 -n package
%setup -q -T -D -a 3 -n package

%patch0 -p1

sed -i '1s/env //' bin/svgo

%nodejs_fixdep coa
%nodejs_fixdep csso
%nodejs_fixdep js-yaml
%nodejs_fixdep sax '^0.6.0'
%nodejs_fixdep colors '^1.1.2'


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json .svgo.yml lib/ plugins/ docs/ examples/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}/bin
install -p -D -m0755 bin/svgo %{buildroot}%{nodejs_sitelib}/%{packagename}/bin/svgo

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/%{packagename}/bin/svgo \
    %{buildroot}%{_bindir}/svgo

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
%doc *.md docs/ examples/
%license LICENSE
%{nodejs_sitelib}/%{packagename}
%{_bindir}/svgo



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Tom Hughes <tom@compton.nu> - 0.7.2-3
- Relax npm(colors) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jared Smith <jsmith@fedoraproject.org> - 0.7.2-1
- Update to upstream 0.7.2 release

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-4
- Add .yml file

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-3
- Fix some dependency versions

* Sun Jul 24 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-2
- Fix tests so that the run correctly

* Sat Jul 23 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.6-1
- Update to upstream 0.6.6 release

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.5.6-1
- Initial packaging
