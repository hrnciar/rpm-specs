%{?nodejs_find_provides_and_requires}

Name:       nodejs-bindings
Version:    1.3.0
Release:    6%{?dist}
Summary:    Helper module for loading your native module's .node file
# License text is included in README.md
License:    MIT
URL:        https://github.com/TooTallNate/node-bindings
Source0:    https://registry.npmjs.org/bindings/-/bindings-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
This is a helper module for authors of Node.js native addon modules.
It is basically the "swiss army knife" of require()ing your native module's
.node file.

Throughout the course of Node's native addon history, addons have ended up
being compiled in a variety of different places, depending on which build tool
and which version of node was used. To make matters worse, now the gyp build
tool can produce either a Release or Debug build, each being built into
different locations.

This module checks all the possible locations that a native addon would be
built at, and returns the first one that loads successfully.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/bindings
cp -pr package.json bindings.js \
    %{buildroot}%{nodejs_sitelib}/bindings

%nodejs_symlink_deps


%files
%doc README.md
%{nodejs_sitelib}/bindings


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jared Smith <jsmith@fedoraproject.org> - 1.3.0-1
- Update to upstream 1.3.0 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 1.2.1-1
- update to 1.2.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-1
- update to upstream release 1.2.0

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.1-1
- new upstream release 1.1.1

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2
- add macro to enable dependency generation in EPEL

* Fri Mar 15 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.1.0-1
- update to upstream release 1.1.0

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0-1
- initial package
