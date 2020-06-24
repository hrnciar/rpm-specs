%{?nodejs_find_provides_and_requires}

Name:       nodejs-require-cs
Version:    0.4.4
Release:    12%{?dist}
Summary:    An AMD loader plugin for CoffeeScript
# Upstream have been informed of missing licenses:
# https://github.com/jrburke/require-cs/issues/44
License:    MIT or BSD
URL:        https://github.com/jrburke/require-cs
Source0:    https://github.com/jrburke/require-cs/archive/%{version}.tar.gz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

# package.json declares the name as 'cs', but this name is already taken in
# the npm registry so rename to 'require-cs' instead.
Patch0:     %{name}-0.4.3-change-name.patch

BuildRequires:  nodejs-packaging
# We are symlinking to these files, so explicitly depend on them just in case
# the packages that own them decide to move them somewhere else.
Requires:       /usr/share/javascript/coffee-script/coffee-script.js
Requires:       /usr/lib/node_modules/requirejs/bin/r.js

%description
A CoffeeScript loader plugin that may work with module loaders like
RequireJS, curl and backdraft.

This loader plugin makes it easy to write your JS functionality in
CoffeeScript, and easily use it in the browser, Node or Rhino. Plus,
if you use the RequireJS optimizer, your CoffeeScript files can be
translated to JavaScript and in-lined into optimized layers for fast
performance.


%prep
%setup -q -n require-cs-%{version}
%patch0 -p1
rm -f coffee-script.js
rm -rf tools/


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/require-cs
cp -pr package.json cs.js \
    %{buildroot}%{nodejs_sitelib}/require-cs

# Replace bundled coffee-script.js with symlink.
ln -sf %{_jsdir}/coffee-script/coffee-script.js \
    %{buildroot}%{nodejs_sitelib}/require-cs/coffee-script.js

# Replace bundled tools/r.js with symlink.
mkdir -p %{buildroot}%{nodejs_sitelib}/require-cs/tools
ln -sf %{nodejs_sitelib}/requirejs/bin/r.js \
    %{buildroot}%{nodejs_sitelib}/require-cs/tools/r.js

%nodejs_symlink_deps


%files
%doc LICENSE README.md demo/ demoserver.js
%{nodejs_sitelib}/require-cs


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Tom Hughes <tom@compton.nu> - 0.4.4-4
- use new location for coffee-script files

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4-1
- update to upstream release 0.4.4
- restrict to compatible arches
- upstream have now included a LICENSE file so use that instead

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-2
- add copies of the MIT and BSD licenses to comply with licensing requirements

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.3-1
- initial package
