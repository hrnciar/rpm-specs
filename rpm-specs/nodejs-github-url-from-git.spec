%{?nodejs_find_provides_and_requires}

Name:           nodejs-github-url-from-git
Version:        1.5.0
Release:        7%{?dist}
Summary:        Parse a GitHub git URL and return the GitHub repository URL

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

#No license file included, "MIT" indicated in README and package.json
#A copy of the MIT license based on the version included with express, another
#node module by the same author, is included in Source1, and has been sent
#upstream: https://github.com/visionmedia/github-url-from-git/pull/5
License:        MIT
URL:            https://github.com/visionmedia/node-github-url-from-git
Source0:        https://registry.npmjs.org/github-url-from-git/-/github-url-from-git-%{version}.tgz
Source1:        https://raw.github.com/tchollingsworth/node-github-url-from-git/154fb09296b79637e25952638782995ad6812612/LICENSE

BuildRequires:  nodejs-packaging

#for tests
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
BuildRequires:  npm(better-assert)

%description
%{summary}.

%prep
%setup -q -n package

#copy LICENSE file into %%_builddir so it works with %%doc
cp %{SOURCE1} LICENSE

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/github-url-from-git
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/github-url-from-git

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
mocha test.js --reporter spec --require should

%files
%{nodejs_sitelib}/github-url-from-git
%doc *.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 08 2017 Jared Smith <jsmith@fedoraproject.org> - 1.5.0-1
- Update to uptream 1.5.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-7
- cleanup spec

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-2
- restrict to compatible arches

* Sun Jun 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- initial package
