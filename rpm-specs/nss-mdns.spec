Name: nss-mdns
Version: 0.14.1
Release: 7%{?dist}
Summary: glibc plugin for .local name resolution

License: LGPLv2+
URL: https://github.com/lathiat/nss-mdns
Source0: https://github.com/lathiat/nss-mdns/releases/download/v%{version}/nss-mdns-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(check)
Requires: avahi

%description
nss-mdns is a plugin for the GNU Name Service Switch (NSS) functionality of
the GNU C Library (glibc) providing host name resolution via Multicast DNS
(aka Zeroconf, aka Apple Rendezvous, aka Apple Bonjour), effectively allowing
name resolution by common Unix/Linux programs in the ad-hoc mDNS domain .local.

nss-mdns provides client functionality only, which means that you have to
run a mDNS responder daemon separately from nss-mdns if you want to register
the local host name via mDNS (e.g. Avahi).


%prep
%autosetup

%build
%configure --libdir=/%{_lib}
%make_build

%check
make check || (cat ./test-suite.log; false)

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%post
%{?ldconfig}

%posttrans
function mod_nss() {
    if [ -f "$1" ] ; then
        # sed-fu to add mdns4_minimal to the hosts line of /etc/nsswitch.conf
	    sed -i.bak '
		    /^hosts:/ !b
    		/\<mdns\(4\|6\)\?\(_minimal\)\?\>/ b
    		s/\([[:blank:]]\+\)dns\>/\1mdns4_minimal [NOTFOUND=return] dns/g
    		' "$1"
    fi
}

FILE="$(readlink /etc/nsswitch.conf || echo /etc/nsswitch.conf)"
if [ "$FILE" = "/etc/authselect/nsswitch.conf" ] && authselect check &>/dev/null; then
    mod_nss "/etc/authselect/user-nsswitch.conf"
    authselect apply-changes &> /dev/null || :
else
    mod_nss "$FILE"
    # also apply the same changes to user-nsswitch.conf to affect
    # possible future authselect configuration
    mod_nss "/etc/authselect/user-nsswitch.conf"
fi

%preun
function mod_nss() {
    if [ -f "$1" ] ; then
        # sed-fu to remove mdns4_minimal from the hosts line of /etc/nsswitch.conf
    	sed -i.bak '
	    	/^hosts:/ !b
		    s/[[:blank:]]\+mdns\(4\|6\)\?\(_minimal\( \[NOTFOUND=return\]\)\?\)\?//g
    		' "$1"
    fi
}

if [ "$1" -eq 0 ] ; then
    FILE="$(readlink /etc/nsswitch.conf || echo /etc/nsswitch.conf)"
    if [ "$FILE" = "/etc/authselect/nsswitch.conf" ] && authselect check &>/dev/null; then
        mod_nss "/etc/authselect/user-nsswitch.conf"
        authselect apply-changes &> /dev/null || :
    else
        mod_nss "$FILE"
        # also apply the same changes to user-nsswitch.conf to affect
        # possible future authselect configuration
        mod_nss "/etc/authselect/user-nsswitch.conf"
    fi
fi

%ldconfig_postun


%files
%license LICENSE
%doc README.md NEWS.md ACKNOWLEDGEMENTS.md
/%{_lib}/*.so.*


%changelog
* Tue Mar 17 2020 Pavel Březina <pbrezina@redhat.com> - 0.14.1-7
- Do not remove mdns from nsswitch.conf during upgrade

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Adam Goode <adam@spicenitz.org> - 0.14.1-5
- Properly work with or without authselect (BZ #1577243)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Adam Goode <adam@spicenitz.org> - 0.14.1-1
- New upstream release
- Modernize the spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Stepan Kasal <skasal@redhat.com> - 0.10-6
- use sed instead of perl in %%post and %%preun (#462996),
  fixing two bugs in the scriptlets:
  1) the backup file shall be nsswitch.conf.bak, not nsswitch.confbak
  2) the first element after host: shall be subject to removal, too
- consequently, removed the Requires(..): perl
- removed the reqires for things that are granted
- a better BuildRoot

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.10-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.10-3
- Rebuild for selinux ppc32 issue.

* Fri Jun 22 2007 - Lennart Poettering <lpoetter@redhat.com> - 0.10-2
- Fix up post/preun/postun dependencies, add "avahi" to the dependencies,
  include dist tag in Release field, use _lib directory instead of literal /lib.

* Fri Jun 22 2007 - Lennart Poettering <lpoetter@redhat.com> - 0.10-1
- Update to 0.10, replace perl script by simpler and more robust versions,
  stolen from the Debian package

* Thu Jul 13 2006 - Bastien Nocera <hadess@hadess.net> - 0.8-2
- Make use of Ezio's perl scripts to enable and disable mdns4 lookups
  automatically, patch from Pancrazio `Ezio' de Mauro <pdemauro@redhat.com>

* Tue May 02 2006 - Bastien Nocera <hadess@hadess.net> - 0.8-1
- Update to 0.8, disable legacy lookups so that all lookups are made through
  the Avahi daemon

* Mon Apr 24 2006 - Bastien Nocera <hadess@hadess.net> - 0.7-2
- Fix building on 64-bit platforms

* Tue Dec 13 2005 - Bastien Nocera <hadess@hadess.net> - 0.7-1
- Update to 0.7, fix some rpmlint errors

* Thu Nov 10 2005 - Bastien Nocera <hadess@hadess.net> - 0.6-1
- Update to 0.6

* Tue Dec 07 2004 - Bastien Nocera <hadess@hadess.net> 0.1-1
- Initial package, automatically adds and remove mdns4 as a hosts service
