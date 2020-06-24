# Bundling request for bootstrap/patternfly: https://fedorahosted.org/fpc/ticket/483

%global snapdate 20200618
%global commit c90a76b2063eb99b944dbe15a1599e527626a4bd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# post-release format...
%global snaprel %{?snapdate:.git%{snapdate}.%{shortcommit}}

# for rpmdev-bumpspec
%global baserelease 14

Name:       ipsilon
Version:    2.1.0
Release:    %{baserelease}%{?snaprel}%{?dist}
Summary:    An Identity Provider Server

License:    GPLv3+
URL:        https://pagure.io/ipsilon
%if %{defined snaprel}
Source0:    %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:    http://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
%endif

# Fedora-specific fixes
## Temporarily revert file path changes, those are for Ipsilon 3.0 release
Patch1001:  1001-Revert-Move-Ipsilon-libexec-content-to-a-subdirector.patch

BuildArch:  noarch


BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-lasso
BuildRequires:  python3-openid, python3-openid-cla, python3-openid-teams
BuildRequires:  python3-m2crypto

Requires:       python3-setuptools
Requires:       python3-requests
Requires:       %{name}-base = %{version}-%{release}

%description
Ipsilon is a multi-protocol Identity Provider service. Its function is to
bridge authentication providers and applications to achieve Single Sign On
and Federation.


%package base
Summary:        Ipsilon base IDP server
License:        GPLv3+
Requires:       httpd
Requires:       mod_ssl
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-provider = %{version}-%{release}
Requires:       python3-mod_wsgi
Requires:       python3-cherrypy
Requires:       python3-jinja2
Requires:       python3-lxml
Requires:       python3-sqlalchemy
Requires:       open-sans-fonts
Requires:       fontawesome-fonts
Requires:       pam
Requires(pre):  shadow-utils

%description base
The Ipsilon IdP server without installer


%package filesystem
Summary:        Package providing files required by Ipsilon
License:        GPLv3+

%description filesystem
Package providing basic directory structure required
for all Ipsilon parts


%package client
Summary:        Tools for configuring Ipsilon clients
License:        GPLv3+
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       %{name}-saml2-base = %{version}-%{release}
Requires:       mod_auth_mellon
Requires:       mod_auth_openidc
Requires:       mod_ssl
Requires:       python3-requests
BuildArch:      noarch

%description client
Client install tools


%package tools-ipa
summary:        IPA helpers
License:        GPLv3+
Requires:       %{name}-authgssapi = %{version}-%{release}
Requires:       %{name}-authform = %{version}-%{release}
Requires:       %{name}-infosssd = %{version}-%{release}
%if 0%{?rhel}
Requires:       ipa-client
Requires:       ipa-admintools
%else
Requires:       freeipa-client
Requires:       freeipa-admintools
%endif
BuildArch:      noarch

%description tools-ipa
Convenience client install tools for IPA support in the Ipsilon identity Provider


%package saml2-base
Summary:        SAML2 base
License:        GPLv3+
Requires:       python3-lasso
Requires:       python3-lxml
BuildArch:      noarch

%description saml2-base
Provides core SAML2 utilities


%package saml2
Summary:        SAML2 provider plugin
License:        GPLv3+
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-saml2-base = %{version}-%{release}
BuildArch:      noarch

%description saml2
Provides a SAML2 provider plugin for the Ipsilon identity Provider


%package openid
Summary:        Openid provider plugin
License:        GPLv3+
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-openid
Requires:       python3-openid-cla
Requires:       python3-openid-teams
BuildArch:      noarch

%description openid
Provides an OpenId provider plugin for the Ipsilon identity Provider

%package openidc
Summary:        OpenID Connect provider plugin
License:        GPLv3+
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-jwcrypto
BuildArch:      noarch

%description openidc
Provides an OpenID Connect and OAuth2 provider plugin for the Ipsilon
identity Provider


%package persona
Summary:        Persona provider plugin
License:        GPLv3+
Provides:       ipsilon-provider = %{version}-%{release}
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-m2crypto
BuildArch:      noarch

%description persona
Provides a Persona provider plugin for the Ipsilon identity Provider


%package authfas
Summary:        Fedora Authentication System login plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-infofas = %{version}-%{release}
Requires:       python3-fedora
BuildArch:      noarch

%description authfas
Provides a login plugin to authenticate against the Fedora Authentication System


%package authform
Summary:        mod_intercept_form_submit login plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       mod_intercept_form_submit
BuildArch:      noarch

%description authform
Provides a login plugin to authenticate with mod_intercept_form_submit


%package authpam
Summary:        PAM based login plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-pam
BuildArch:      noarch

%description authpam
Provides a login plugin to authenticate against the local PAM stack


%package authgssapi
Summary:        mod_auth_gssapi based login plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       mod_auth_gssapi
BuildArch:      noarch

%description authgssapi
Provides a login plugin to allow authentication via the mod_auth_gssapi
Apache module.


%package authldap
Summary:        LDAP info and login plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-ldap
BuildArch:      noarch

%description authldap
Provides a login plugin to allow authentication and info retrieval via LDAP.


%package infofas
Summary:        Fedora Authentication System login plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-fedora
BuildArch:      noarch

%description infofas
Provides an info plugin to retrieve info from the Fedora Authentication System


%package infosssd
Summary:        SSSD based identity plugin
License:        GPLv3+
Requires:       %{name}-base = %{version}-%{release}
Requires:       python3-sssdconfig
Requires:       libsss_simpleifp
Requires:       sssd >= 1.12.4
BuildArch:      noarch

%description infosssd
Provides an info plugin to allow retrieval via SSSD.

%package theme-Fedora
Summary:        Fedora Account System theme
Requires:       %{name}-base = %{version}-%{release}
BuildArch:      noarch

%description theme-Fedora
Provides a theme for Ipsilon used for the Fedora Account System.

%package theme-openSUSE
Summary:        openSUSE Accounts theme
Requires:       %{name}-base = %{version}-%{release}
BuildArch:      noarch

%description theme-openSUSE
Provides a theme for Ipsilon used for openSUSE Accounts.

%prep
%if %{defined snaprel}
%autosetup -n %{name}-%{commit} -p1
%else
%autosetup -p1
%endif


%build
%py3_build


%install
%py3_install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_defaultdocdir}
mkdir -p %{buildroot}%{_localstatedir}/cache/ipsilon
# These 0700 permissions are because ipsilon will store private keys here
install -d -m 0700 %{buildroot}%{_sharedstatedir}/ipsilon
install -d -m 0700 %{buildroot}%{_sysconfdir}/ipsilon
mv %{buildroot}/%{_bindir}/ipsilon %{buildroot}/%{_libexecdir}
mv %{buildroot}/%{_bindir}/ipsilon-server-install %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/ipsilon-upgrade-database %{buildroot}/%{_sbindir}
mv %{buildroot}%{_defaultdocdir}/%{name} %{buildroot}%{_defaultdocdir}/%{name}-%{version}
rm -fr %{buildroot}%{python3_sitelib}/tests
ln -s %{_datadir}/fonts %{buildroot}%{_datadir}/ipsilon/ui/fonts

mkdir -p  %{buildroot}%{_sysconfdir}/pam.d
cp %{buildroot}%{_datadir}/ipsilon/templates/install/pam/ipsilon.pamd %{buildroot}%{_sysconfdir}/pam.d/ipsilon

#%check
# The test suite is not being run because:
#  1. The last step of %%install removes the entire test suite
#  2. It increases build time a lot
#  3. It adds more build dependencies (namely postgresql server and client libraries)

%pre base
getent group ipsilon >/dev/null || groupadd -r ipsilon
getent passwd ipsilon >/dev/null || \
    useradd -r -g ipsilon -d %{_sharedstatedir}/ipsilon -s /sbin/nologin \
    -c "Ipsilon Server" ipsilon
exit 0


%files filesystem
%doc README.md
%license COPYING
%dir %{_datadir}/ipsilon
%dir %{_datadir}/ipsilon/templates
%dir %{_datadir}/ipsilon/templates/install
%dir %{python3_sitelib}/ipsilon
%{python3_sitelib}/ipsilon/__init__.py*
%{python3_sitelib}/ipsilon-*.egg-info
%dir %{python3_sitelib}/ipsilon/__pycache__/
%{python3_sitelib}/ipsilon/__pycache__/__init__.*
%dir %{python3_sitelib}/ipsilon/tools
%{python3_sitelib}/ipsilon/tools/__init__.py*
%{python3_sitelib}/ipsilon/tools/files.py*
%dir %{python3_sitelib}/ipsilon/tools/__pycache__
%{python3_sitelib}/ipsilon/tools/__pycache__/__init__.*
%{python3_sitelib}/ipsilon/tools/__pycache__/files.*

%files
%{_sbindir}/ipsilon-server-install
%{_bindir}/ipsilon-db2conf
%{_datadir}/ipsilon/templates/install/*.conf
%{_datadir}/ipsilon/ui/saml2sp
%dir %{python3_sitelib}/ipsilon/helpers
%{python3_sitelib}/ipsilon/helpers/common.py*
%{python3_sitelib}/ipsilon/helpers/__init__.py*
%dir %{python3_sitelib}/ipsilon/helpers/__pycache__
%{python3_sitelib}/ipsilon/helpers/__pycache__/__init__.*
%{python3_sitelib}/ipsilon/helpers/__pycache__/common.*
%{_mandir}/man*/ipsilon-server-install.1*

%files base
%{_defaultdocdir}/%{name}-%{version}
%{python3_sitelib}/ipsilon/admin
%{python3_sitelib}/ipsilon/authz
%{python3_sitelib}/ipsilon/rest
%{python3_sitelib}/ipsilon/tools/dbupgrade.py*
%{python3_sitelib}/ipsilon/tools/__pycache__/dbupgrade.*
%dir %{python3_sitelib}/ipsilon/login
%{python3_sitelib}/ipsilon/login/__init__*
%{python3_sitelib}/ipsilon/login/common*
%{python3_sitelib}/ipsilon/login/authtest*
%dir %{python3_sitelib}/ipsilon/login/__pycache__
%{python3_sitelib}/ipsilon/login/__pycache__/__init__*
%{python3_sitelib}/ipsilon/login/__pycache__/common*
%{python3_sitelib}/ipsilon/login/__pycache__/authtest*
%dir %{python3_sitelib}/ipsilon/info
%{python3_sitelib}/ipsilon/info/__init__*
%{python3_sitelib}/ipsilon/info/common*
%{python3_sitelib}/ipsilon/info/infonss*
%dir %{python3_sitelib}/ipsilon/info/__pycache__
%{python3_sitelib}/ipsilon/info/__pycache__/__init__*
%{python3_sitelib}/ipsilon/info/__pycache__/common*
%{python3_sitelib}/ipsilon/info/__pycache__/infonss*
%dir %{python3_sitelib}/ipsilon/providers
%{python3_sitelib}/ipsilon/providers/__init__*
%{python3_sitelib}/ipsilon/providers/common*
%dir %{python3_sitelib}/ipsilon/providers/__pycache__
%{python3_sitelib}/ipsilon/providers/__pycache__/__init__*
%{python3_sitelib}/ipsilon/providers/__pycache__/common*
%{python3_sitelib}/ipsilon/root.py*
%{python3_sitelib}/ipsilon/__pycache__/root.*
%{python3_sitelib}/ipsilon/util
%{python3_sitelib}/ipsilon/user
%{_mandir}/man*/ipsilon.7*
%{_mandir}/man*/ipsilon.conf.5*
%{_datadir}/ipsilon/templates/*.html
%{_datadir}/ipsilon/templates/admin
%{_datadir}/ipsilon/templates/user
%dir %{_datadir}/ipsilon/templates/login
%{_datadir}/ipsilon/templates/login/index.html
%{_datadir}/ipsilon/templates/login/form.html
%dir %{_datadir}/ipsilon/ui
%{_datadir}/ipsilon/ui/css
%{_datadir}/ipsilon/ui/img
%{_datadir}/ipsilon/ui/js
%{_datadir}/ipsilon/ui/fonts
%{_datadir}/ipsilon/ui/fonts-local
%{_libexecdir}/ipsilon
%{_sbindir}/ipsilon-upgrade-database
%dir %attr(0751,root,root) %{_sharedstatedir}/ipsilon
%dir %attr(0751,root,root) %{_sysconfdir}/ipsilon
%dir %attr(0750,ipsilon,apache) %{_localstatedir}/cache/ipsilon
%{_sysconfdir}/pam.d/ipsilon
%dir %{_datadir}/ipsilon/themes

%files client
%{_bindir}/ipsilon-client-install
%{_datadir}/ipsilon/templates/install/saml2
%{_datadir}/ipsilon/templates/install/openidc
%{_mandir}/man*/ipsilon-client-install.1*

%files tools-ipa
%{python3_sitelib}/ipsilon/helpers/ipa.py*
%{python3_sitelib}/ipsilon/helpers/__pycache__/ipa.*

%files saml2-base
%{python3_sitelib}/ipsilon/tools/saml2metadata.py*
%{python3_sitelib}/ipsilon/tools/certs.py*
%{python3_sitelib}/ipsilon/tools/__pycache__/saml2metadata.*
%{python3_sitelib}/ipsilon/tools/__pycache__/certs.*

%files saml2
%{python3_sitelib}/ipsilon/providers/saml2*
%{python3_sitelib}/ipsilon/providers/__pycache__/saml2*
%{_datadir}/ipsilon/templates/saml2

%files openid
%{python3_sitelib}/ipsilon/providers/openidp.py*
%{python3_sitelib}/ipsilon/providers/__pycache__/openidp.*
%{python3_sitelib}/ipsilon/providers/openid/
%{python3_sitelib}/ipsilon/providers/openid/__pycache__/
%{_datadir}/ipsilon/templates/openid

%files openidc
%{python3_sitelib}/ipsilon/providers/openidcp.py*
%{python3_sitelib}/ipsilon/providers/__pycache__/openidcp.*
%{python3_sitelib}/ipsilon/providers/openidc/
%{python3_sitelib}/ipsilon/providers/openidc/__pycache__/
%{_datadir}/ipsilon/templates/openidc

%files persona
%{python3_sitelib}/ipsilon/providers/personaidp*
%{python3_sitelib}/ipsilon/providers/__pycache__/personaidp.*
#{_datadir}/ipsilon/templates/persona

%files authfas
%{python3_sitelib}/ipsilon/login/authfas*
%{python3_sitelib}/ipsilon/login/__pycache__/authfas*

%files authform
%{python3_sitelib}/ipsilon/login/authform*
%{python3_sitelib}/ipsilon/login/__pycache__/authform*

%files authpam
%{python3_sitelib}/ipsilon/login/authpam*
%{python3_sitelib}/ipsilon/login/__pycache__/authpam*
%{_datadir}/ipsilon/templates/install/pam

%files authgssapi
%{python3_sitelib}/ipsilon/login/authgssapi*
%{python3_sitelib}/ipsilon/login/__pycache__/authgssapi*
%{_datadir}/ipsilon/templates/login/gssapi.html

%files authldap
%{python3_sitelib}/ipsilon/login/authldap*
%{python3_sitelib}/ipsilon/info/infoldap*
%{python3_sitelib}/ipsilon/login/__pycache__/authldap*
%{python3_sitelib}/ipsilon/info/__pycache__/infoldap*

%files infosssd
%{python3_sitelib}/ipsilon/info/infosssd.*
%{python3_sitelib}/ipsilon/info/__pycache__/infosssd*

%files infofas
%{python3_sitelib}/ipsilon/info/infofas.*
%{python3_sitelib}/ipsilon/info/__pycache__/infofas*

%files theme-Fedora
%{_datadir}/ipsilon/themes/Fedora

%files theme-openSUSE
%{_datadir}/ipsilon/themes/openSUSE


%changelog
* Thu Jun 18 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-14.git20200618.c90a76b
- Bump to new snapshot

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-13.git20200428.f99a7d4
- Rebuilt for Python 3.9

* Tue May 05 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-12.git20200428.f99a7d4
- Bump to new snapshot

* Fri Apr 10 2020 Neal Gompa <ngompa13@gmail.com> - 2.1.0-11.git20200301.171ffda
- Bump to new snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10.git20190910.aa89b1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-9.git20190910.aa89b1f
- Require python3-m2crypto, not just m2crypto (provided by python2-m2crypto)

* Tue Sep 10 2019 Neal Gompa <ngompa13@gmail.com> - 2.1.0-8.git20190910.aa89b1f
- Upgrade to git snapshot release
- Switch to Python 3

* Thu Jul 25 2019 Leigh Scott <leigh123linux@gmail.com> - 2.1.0-7
- Fix build issue

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 15 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.1.0-1
- Rebase to 2.1.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-5
- Removed dependency on mod_lookup_identity

* Tue Feb 14 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-4
- Added dependency on python-setuptools

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 04 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-2
- Add patch to fix RHBZ#1391445

* Thu Nov 24 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.2-1
- Upgrade to 2.0.2

* Mon Oct 31 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.1-1
- New release to enable authz allow on upgrade

* Fri Oct 28 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 2.0.0-1
- Rebase to Ipsilon 2.0.0

* Wed Aug 31 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-7
- Backport ipsilon-upgrade-database fix for configfile

* Wed Aug 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-6
- Move pam file to base package

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-4
- Backport unicode patches (RHBZ#1334637)

* Tue May 10 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-3
- Move user creation to -base subpackage (RHBZ#1334583)

* Tue May 03 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-2
- Install pam file

* Mon May 02 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.2.0-1
- Rebase to upstream 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1.1-2
- Fix files and requires

* Wed Oct 14 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1.1-1
- Rebase to upstream 1.1.1

* Tue Sep 08 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.1.0-1
- Rebased to 1.1.0 release

* Fri Aug 21 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-5
- Backported some patches
- Fix for CVE-2015-5215/CVE-2015-5216/CVE-2015-5217

* Tue Aug 11 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-4
- Remove the gpg check

* Mon Jun 22 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-3
- Add mod_ssl dependency on ipsilon-client

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 11 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.0.0-1
- Update to release 1.0.0

* Mon Apr 20 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.6.0-1
- Update to release 0.6.0

* Mon Mar 30 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.5.0-1
- Update to release 0.5.0

* Mon Mar 02 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.4.0-1
- Update to release 0.4.0

* Wed Jan 28 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-5
- Split IPA tools

* Mon Jan 12 2015 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-4
- Add symlink to fonts directory

* Tue Dec 16 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-3
- Fix typo
- Add comments on why the test suite is not in check
- The subpackages require the base package
- Add link to FPC ticket for bundling exception request

* Tue Dec 16 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-2
- Fix shebang removal

* Tue Dec 16 2014 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.3.0-1
- Initial packaging
