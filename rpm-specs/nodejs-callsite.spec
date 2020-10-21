%{?nodejs_find_provides_and_requires}

#use a github tarball so we get the tests
%global commit 8d3927995821596148e77f4af049ab38b03d1b99
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           nodejs-callsite
Version:        1.0.0
Release:        17%{?dist}
Summary:        Provides access to V8's "raw" CallSites from Node.js

#No license file included, "MIT" indicated in README and package.json
#A copy of the MIT license based on the version included with express, another
#node module by the same author, is included in Source1, and has been sent
#upstream: https://github.com/visionmedia/callsite/pull/2
License:        MIT
URL:            https://github.com/visionmedia/callsite
Source0:        https://github.com/visionmedia/callsite/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        https://raw.github.com/tchollingsworth/callsite/8d7615a28a6507c3ef0731f072d3f1a100b3fe27/LICENSE

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# Fix the tests to comply with modern "should" syntax and with changes
# to the callsite code itself
Patch1:         %{name}_fix-tests.patch

BuildRequires:  nodejs-devel

#for tests
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)

%description
%{summary}.

This is useful for custom traces, C-style assertions, getting the line number in
execution, and more.


%prep
%setup -q -n callsite-%{commit}

#fix tests
%patch1 -p1

#copy LICENSE file into %%_builddir so it works with %%doc
cp %{SOURCE1} LICENSE


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/callsite
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/callsite
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
mocha --require should


%files
%doc Readme.md examples History.md
%license LICENSE
%{nodejs_sitelib}/callsite


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 1.0.0-7
- Cleanup spec file, removing %%defattr

* Mon Jan 25 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-6
- Fix tests to build with newer version of nodejs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-2
- restrict to compatible arches

* Sun Jun 02 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
