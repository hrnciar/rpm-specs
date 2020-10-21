# Provenpackagers are welcome to modify this package, but please don't obsolete
# additional packages without a corresponding bugzilla ticket being filed.

# Please remember to add all of the necessary information.  See below the
# Source0: line for a description of the format.  It is important that
# everything be included; yanking packages from an end-user system is "serious
# business" and should not be done lightly or without making everything as
# clear as possible.

# Finally, please keep python2 obsoletes together, since there is bound to be a
# significant number of them.

Name:       fedora-obsolete-packages
# Please keep the version equal to the targeted Fedora release
Version:    34
Release:    8
Summary:    A package to obsolete retired packages

# This package has no actual content; there is nothing to license.
License:    Public Domain
URL:        https://docs.fedoraproject.org/en-US/packaging-guidelines/#renaming-or-replacing-existing-packages
BuildArch:  noarch

Source0:    README

# ===============================================================================
# Skip down below these convenience macros
%define obsolete_ticket() %{lua:
    local ticket = rpm.expand('%1')

    -- May need to declare the master structure
    if type(obs) == 'nil' then
        obs = {}
    end

    if ticket == '%1' then
        rpm.expand('%{error:No ticket provided to obsolete_ticket}')
    end

    if ticket == 'Ishouldfileaticket' then
        ticket = nil
    end

    -- Declare a new set of obsoletes
    local index = #obs+1
    obs[index] = {}
    obs[index].ticket = ticket
    obs[index].list = {}
}

%define obsolete() %{lua:
    local pkg = rpm.expand('%1')
    local ver = rpm.expand('%2')
    local pkg_
    local ver_
    local i
    local j

    if pkg == '%1' then
        rpm.expand('%{error:No package name provided to obsolete}')
    end
    if ver == '%2' then
        rpm.expand('%{error:No version provided to obsolete}')
    end

    if not string.find(ver, '-') then
        rpm.expand('%{error:You must provide a version-release, not just a version.}')
    end

    print('Obsoletes: ' .. pkg .. ' < ' .. ver)

    -- Check if the package wasn't already obsoleted
    for i = 1,#obs do
        for j = 1,#obs[i].list do
            pkg_, ver_ = table.unpack(obs[i].list[j])
            if pkg == pkg_ then
                rpm.expand('%{error:' .. pkg ..' obsoleted multiple times (' .. ver_ .. ' and ' .. ver ..').}')
            end
        end
    end

    -- Append this obsolete to the last set of obsoletes in the list
    local list = obs[#obs].list
    list[#list+1] = {pkg, ver}
}

%define list_obsoletes %{lua:
    local i
    local j
    for i = 1,#obs do
        if obs[i].ticket ~= nil and string.find(obs[i].ticket, '1578359') then
            print('Plus the following python2 packages, in accordance with the general switch away\\n')
            print('from Python2 ahead of its retirement in 2020.  See\\n')
            print('https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3 for more\\n')
            print('information.\\n\\n')
        end

        for j = 1,#obs[i].list do
            pkg, ver = table.unpack(obs[i].list[j])
            print('  ' .. pkg .. ' < ' .. ver .. '\\n')
        end
        if obs[i].ticket == nil then
            print('  (No ticket was provided!)\\n\\n')
        else
            print('  (See ' .. obs[i].ticket .. ')\\n\\n')
        end
    end
}

# ===============================================================================
# Add calls to the obsolete_ticket and obsolete macros below, along with a note
# indicating the Fedora version in which the entries can be removed.  This is
# generally three releases beyond whatever release Rawhide is currently.  The
# macros make this easy, and will automatically update the package description.

# The ticket information is important.  Please don't add things here without
# having a filed ticket, preferrably in bugzilla.

# All Obsoletes: entries MUST be versioned (including the release), with the
# version being the same as or just higher than the last version-release of the
# obsoleted package.  This allows the package to return to the distribution
# later.  The best possible thing to do is to find the last version-release
# which was in the distribution, add one to the release, and add that version
# without using a dist tag.  This allows a rebuild with a bumped Release: to be
# installed.

# And don't forget to update the package description!


# Template:
# Remove in F36
# %%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# %%obsolete foo 3.5-7

# ========================================
# Please place non-python Obsoletes: here
# ========================================

# Remove in F35
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1781359
%obsolete epiphany-runtime 1:3.36.99-1

# Remove in F35
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1862511
%obsolete libcroco 0.6.13-5
%obsolete libcroco-devel 0.6.13-5
%obsolete hippo-canvas 0.3.0-30

# Remove in F35
%obsolete_ticket https://src.fedoraproject.org/rpms/infinispan/c/b2c5a112eff72b01d005dc58522ca5579739a8f8
%obsolete infinispan 8.2.4-6

# Perl 5.30
# Remove in F35
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1884617
%obsolete glite-lb-types 2.0.10-18
%obsolete gpsdrive 2.11-54
%obsolete mirrorbrain-scanner 2.18.1-27
%obsolete opendchub 0.8.3-20
%obsolete perl-CPAN-Reporter 1.2018-12
%obsolete perl-Compress-LZ4 0.25-12
%obsolete perl-Compress-Snappy 0.24-16
%obsolete perl-Crypt-PBKDF2 0.161520-12
%obsolete perl-Crypt-Random-TESHA2 0.01-16
%obsolete perl-Crypt-SaltedHash 0.09-18
%obsolete perl-Date-Easter 1.22-16
%obsolete perl-Digest-Bcrypt 1.209-11
%obsolete perl-Digest-PBKDF2 0.013-9
%obsolete perl-Filesys-SmbClient 3.2-22
%obsolete perl-GStreamer 0.20-18
%obsolete perl-Geo-Point 0.98-4
%obsolete perl-Geo-Proj4 1.09-4
%obsolete perl-Image-SubImageFind 0.03-23
%obsolete perl-Module-Data 0.013-11
%obsolete perl-Parse-CPAN-Packages-Fast 0.09-14
%obsolete perl-Path-ScanINC 1.000003-11
%obsolete perl-Pod-Wordlist-hanekomu 1.132680-25
%obsolete perl-SOCKS 0.03-17
%obsolete perl-Test2-Plugin-SpecDeclare 0.000003-12
%obsolete perl-Time-TAI64 2.11-16
%obsolete perl-X11-GUITest 0.28-20
%obsolete perl-perl5i 2.13.2-14
%obsolete perl-qpid-messaging 1.39.0-6
%obsolete perl-re-engine-PCRE2 0.16-5
%obsolete perl-sword 1.8.1-20
%obsolete zanata-util 0.2.9-20

# ==========================================
# Please collect the python 3.8 Obsoletes: here
# ==========================================

# Remove in F35
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1856098
%obsolete antimony 0.9.3-18
%obsolete boost169-numpy3 1.69.0-7
%obsolete boost169-python3 1.69.0-7
%obsolete coreboot-utils 4.11-2
%obsolete csvdiff 0.3.1-12
%obsolete gfal2-util 1.5.3-7
%obsolete hovercraft 2.2-10
%obsolete inception 0.4.1-16
%obsolete mnemosyne 2.6.1-5
%obsolete modtools 0.0.1-13
%obsolete mozilla-iot-gateway-addon-python 0.9.0-3
%obsolete python-bna 4.1.0-15
%obsolete python-ladon 0.9.38-13
%obsolete python3-args 0.1.0-15
%obsolete python3-asynctest 0.13.0-5
%obsolete python3-avocado-vt 77.0-2
%obsolete python3-bashate 0.5.1-15
%obsolete python3-blist 1.3.6-25
%obsolete python3-blockdiag-devel 2.0.0-3
%obsolete python3-cantor 19.12.2-3
%obsolete python3-clint 0.5.1-16
%obsolete python3-cltk 0.1.111-3
%obsolete python3-configparser 3.7.1-8
%obsolete python3-couchdb 1.0-18
%obsolete python3-django-babel 0.6.2-12
%obsolete python3-django-simple-captcha 0.5.6-11
%obsolete python3-django-tinymce 2.4.0-14
%obsolete python3-flask-cache 0.13.1-20
%obsolete python3-flower 0.9.2-8
%obsolete python3-gerrit-view 0.4.6-5
%obsolete python3-gofer-qpid 3.0.0-0.7
%obsolete python3-heketi 9.0.0-6
%obsolete python3-hug 2.4.0-5
%obsolete python3-invocations 0.13.0-16
%obsolete python3-jupyterlab-launcher 0.11.0-8
%obsolete python3-line_profiler 2.1-8
%obsolete python3-multio 0.2.4-7
%obsolete python3-neomodel 3.3.1-7
%obsolete python3-nistats 0.0.1-0.6
%obsolete python3-nnpy 1.4.2-6
%obsolete python3-nose-xcover 1.0.11-8
%obsolete python3-nose_warnings_filters 0.1.5-13
%obsolete python3-openslide 1.1.1-19
%obsolete python3-pathlib2 2.3.5-3
%obsolete python3-pip-shims 0.3.2-5
%obsolete python3-poppler-qt4 0.18.1-22
%obsolete python3-pyephem 3.7.6.0-19
%obsolete python3-pykmip 0.8.0-6
%obsolete python3-pythonfinder 1.2.1-5
%obsolete python3-radicale 2.1.12-4
%obsolete python3-readme_renderer 24.0-7
%obsolete python3-social-auth-app-flask 1.0.0-9
%obsolete python3-social-auth-app-flask-sqlalchemy 1.0.1-9
%obsolete python3-social-auth-storage-sqlalchemy 1.1.0-9
%obsolete python3-sphinxcontrib-fulltoc 1.2-13
%obsolete python3-tgext-crud 0.8.2-10
%obsolete python3-traceback2 1.4.0-27
%obsolete python3-txamqp 0.8.1-13
%obsolete python3-unittest2 1.1.0-25
%obsolete python3-vistir 0.4.3-6
%obsolete python3-yaspin 0.14.3-6
%obsolete sse2fedmsg 0.3.0-10
%obsolete subscription-manager-migration 1.25.9-6
%obsolete ubertooth-specan-ui 2018.12.R1-9


# ==========================================
# Please collect the python2 Obsoletes: here
# ==========================================

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1578359

# Remove in F35
%obsolete python2-authres 1.2.0-7
%obsolete python2-docutils 0.15.2-5
%obsolete python2-libxml2 2.9.10-5
%obsolete python2-pycryptodomex 3.9.8-2
%obsolete python2-pycryptodomex-selftest 3.9.8-2
%obsolete python2-typing 3.7.4.1-3
%obsolete trac-CGit-plugin 1.0.6-15
%obsolete trac-blackmagictickettweaks-plugin 0.12.3-5
%obsolete trac-sensitivetickets-plugin 0.21-16


# Don't put non-Python obsoletes here, there is a section above

# This package won't be installed, but will obsolete other packages
Provides: libsolv-self-destruct-pkg()

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

Currently obsoleted packages:

%list_obsoletes


%prep
%autosetup -c -T
cp %SOURCE0 .


%files
%doc README


%changelog
* Thu Oct 08 2020 Miro Hrončok <mhroncok@redhat.com> - 34-8
- Obsolete hippo-canvas (#1884548)
- Update the list of obsoleted Python 2 packages
- Obsolete removed packages that used to require Perl 5.30 (#1884617)
- Update the list of obsoleted Python 3.8 packages (#1856098)

* Mon Oct 05 2020 Petr Pisar <ppisar@redhat.com> - 34-7
- Update python2-libxml2 version

* Mon Oct 05 2020 Petr Pisar <ppisar@redhat.com> - 34-6
- Obsolete perl-Digest-Bcrypt and python2-libxml2

* Sat Sep 19 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 34-5
- Obsolete zanata-util and infinispan

* Fri Sep 18 2020 Miro Hrončok <mhroncok@redhat.com> - 34-4
- Update list of packages with broken dependency on Python 3.8 (#1856098)

* Wed Sep 09 2020 Kalev Lember <klember@redhat.com> - 34-3
- Obsolete libcroco-devel as well

* Thu Aug 20 2020 Miro Hrončok <mhroncok@redhat.com> - 34-2
- Bump epiphany-runtime version (#1869324)
- Update list of packages with broken dependency on Python 3.8 (#1856098)

* Tue Aug 11 2020 Miro Hrončok <mhroncok@redhat.com> - 34-1
- Clean for Fedora 34

* Tue Aug 11 2020 Michael Catanzaro <mcatanzaro@gnome.org> - 33-21
- Obsolete libcroco (#1862511)

* Mon Aug 10 2020 Miro Hrončok <mhroncok@redhat.com> - 33-20
- Update list of Python 2 packages with broken dependencies

* Mon Aug 10 2020 Miro Hrončok <mhroncok@redhat.com> - 33-19
- Update list of packages with broken dependency on Python 3.8 (#1856098)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 33-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Miro Hrončok <mhroncok@redhat.com> - 33-17
- Obsolete python2-pillow-devel (#1858557)
- Bump version of python2-pillow-tk and -qt

* Sun Jul 19 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 33-16
- Bump Obsoletes for python2-beautifulsoup4

* Sun Jul 12 2020 Miro Hrončok <mhroncok@redhat.com> - 33-15
- Obsolete removed packages with broken dependency on Python 3.8 (#1856098)

* Wed May 20 2020 Miro Hrončok <mhroncok@redhat.com> - 33-14
- Update and add more Python 2 packages (#1837981)

* Wed May 06 2020 Miro Hrončok <mhroncok@redhat.com> - 33-13
- Stop obsoleting gstreamer packages already obsoleted by the repo they are from (#1822597)

* Fri May 01 2020 Miro Hrončok <mhroncok@redhat.com> - 33-12
- Bump versions of python2-beautifulsoup4 and python2-matplotlib (#1830231)

* Thu Apr 23 2020 Miro Hrončok <mhroncok@redhat.com> - 33-11
- Obsolete mod_auth_kerb (#1827417)

* Fri Apr 17 2020 Miro Hrončok <mhroncok@redhat.com> - 33-10
- Obsolete more removed Python 3.7 packages and remove the resurrected ones

* Mon Apr 06 2020 Miro Hrončok <mhroncok@redhat.com> - 33-9
- Update playonlinux version
- Update python2-qpid-proton version
- Obsolete epiphany-runtime (#1781359)
- Add back SELinux related Python 2 packages (#1821357)

* Wed Mar 18 2020 Miro Hrončok <mhroncok@redhat.com> - 33-8
- Fix the version of obsoleted python2-soupsieve (#1814543)
- Obsolete gradle (#1813401)

* Tue Mar 17 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 33-7
- Obsolete postgresql-plruby

* Thu Mar 12 2020 Miro Hrončok <mhroncok@redhat.com> - 33-6
- Obsolete js-moment

* Thu Mar 12 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 33-5
- Obsolete blueproximity

* Mon Mar 09 2020 Lukas Zapletal <lzap+rpm@redhat.com> 33-5
- Obsolete decibel-audio-player

* Sun Mar  8 2020 Peter Robinson <pbrobinson@fedoraproject.org> 33-4
- Obsolete gnome2-python bits

* Thu Mar 05 2020 Miro Hrončok <mhroncok@redhat.com> - 33-3
- Obsolete playonlinux, system-config-keyboard, wxPython-devel, gnome-python2-desktop
- Update versions of exaile, python2-fmf, python2-txws, python2-txzmq, python2-pyyaml

* Mon Mar 02 2020 Miro Hrončok <mhroncok@redhat.com> - 33-2
- Update the list of obsoleted Python packages

* Tue Feb 25 2020 Miro Hrončok <mhroncok@redhat.com> - 33-1
- Cleaned up for Fedora 33

* Tue Feb 25 2020 Miro Hrončok <mhroncok@redhat.com> - 32-36
- Obsolete (hopefully) all problematic removed Python 2 packages

* Tue Feb 25 2020 Miro Hrončok <mhroncok@redhat.com> - 32-35
- Obsolete more Python 3.7 packages

* Wed Feb 19 2020 Pete Walter <pwalter@fedoraproject.org> - 32-34
- Obsolete python2-fedora

* Wed Feb 19 2020 Pete Walter <pwalter@fedoraproject.org> - 32-33
- Obsolete gstreamer 0.10 packages
- Obsolete farstream
- Obsolete python2-dmidecode, python2-libuser

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 32-32
- Add a few more python2 obsoletes

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 32-31
- Fix packagedb-cli obsoletes version
- Fix python2-koji obsoletes version
- Fix python2-libxml2 obsoletes version

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 32-30
- Re-add compat-gnutls28, libsilc, pam_pkcs11 obsoletes

* Tue Jan 28 2020 Miro Hrončok <mhroncok@redhat.com> - 32-29
- Obsolete more Python 3.7 packages

* Sun Jan 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 32-28
- Obsolete python2-abiword python2-xapian

* Tue Dec 03 2019 Miro Hrončok <mhroncok@redhat.com> - 32-27
- Obsolete python2-os-client-config (#1747436)
- Obsolete python2-simplemediawiki (#1767495)
- Obsolete python2-pep8 (#1779378)
- Obsolete python2-libxml2 (#1776795)

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 32-26
- Remove gedit-plugin-synctex obsolete as it was re-added in gedit-plugins 3.34.1

* Thu Nov 21 2019 Miro Hrončok <mhroncok@redhat.com> - 32-25
- Obsolete python2-migrate (#1775389)

* Mon Nov 18 2019 Miro Hrončok <mhroncok@redhat.com> - 32-24
- Update the list of obsoletes Python 3.7 packages
- Obsolete python2-gwebsockets, python2-wxpython4

* Tue Nov 12 08:16:26 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 32-23
- Mark this package as self-destruct

* Thu Nov  7 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-22
- Also obsolete other binary packages of zanata-platform

* Sat Oct 26 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-21
- Obsolete zanata-platform
- Obsolete maven-site-plugin (#1755570)
- Obsolete CGAL (#1757792)
- Obsolete a bunch of python3 packages that require python3.7 and break
  the upgrade path after the switch to python3.8 (#1754151)
- Obsolete python3-sip (#1753069)

* Wed Oct 23 2019 Miro Hrončok <mhroncok@redhat.com> - 32-20
- Obsolete system-config-users-docs (#1751252)

* Tue Oct 08 2019 Miro Hrončok <mhroncok@redhat.com> - 32-19
- Update obsoleted Python 3.7 packages (#1754151)

* Mon Sep 23 2019 Miro Hrončok <mhroncok@redhat.com> - 32-18
- Obsolete removed packages that depend on Python 3.7 (#1754151)

* Fri Sep 20 2019 Pete Walter <pwalter@fedoraproject.org> - 32-17
- Bump python2-policycoreutils obsoletes version

* Wed Sep 18 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl>
- Obsolete fedora-release-notes, mono-debugger, python2-pillow-{tk,qt}

* Thu Sep 12 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-15
- Obsolete a bunch of python2 packages based on testing the upgrade
  path from F30 to F31.

* Thu Sep 12 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-14
- Obsolete a bunch of packages based on fedora-devel feedback
  (#1751418, #1751419, #1751345)

* Wed Sep 11 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-13
- Obsolete a bunch of packages (#1684162, #1750135, #1751211,
				##1750138, #1578359, #1750660)

* Wed Sep 11 2019 Miro Hrončok <mhroncok@redhat.com> - 32-12
- Fix a typo in gcompris (#1747430)

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-11
- Obsolete fedmsg-notify (#1644813), gcompris (#1747430)

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-10
- Obsolete python2-pandas-datareader

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 32-9
- Obsolete gegl (#1747428)

* Fri Aug 30 2019 Miro Hrončok <mhroncok@redhat.com> - 32-8
- Obsolete python2-cliff, python2-copr, python2-docker, python2-fedmsg,
  python2-future, python2-grokmirror, python2-keystoneauth1, python2-markdown,
  python2-openstacksdk, python2-pwquality, python2-warlock, system-config-users
  (#1747436)

* Fri Aug 30 2019 Pete Walter <pwalter@fedoraproject.org> - 32-7
- Obsolete python2-rabbitvcs (#1738183)

* Mon Aug 26 2019 Neal Gompa <ngompa13@gmail.com> - 32-6
- Obsolete oggconvert

* Sun Aug 25 2019 Kalev Lember <klember@redhat.com> - 32-5
- Obsolete gedit-plugin-synctex

* Sun Aug 25 2019 Kalev Lember <klember@redhat.com> - 32-4
- Obsolete python2-unbound

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 32-3
- Obsolete python3-importlib-metadata (#1725789)

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 32-2
- Obsolete python2-libselinux and python2-libsemanage

* Tue Aug 13 2019 Miro Hrončok <mhroncok@redhat.com> - 32-1
- Cleaned up for Fedora 32

* Tue Aug 13 2019 Miro Hrončok <mhroncok@redhat.com> - 31-20
- Obsolete a batch of problematic python2 packages removed in Fedora 31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 31-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Miro Hrončok <mhroncok@redhat.com> - 31-18
- Obsolete python2-langtable (#1706075)

* Tue May 21 2019 Miro Hrončok <mhroncok@redhat.com> -31-17
- Obsolete yumex (#1707567)
- Obsolete pix (#1707570)
- Obsolete system-config-services (#1707577)

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 31-16
- Bump python2-hawkey, python2-libdnf and python2-solv versions (#1632564)

* Thu Apr 25 2019 Kalev Lember <klember@redhat.com> - 31-15
- Obsolete california (#1702954)

* Mon Apr 22 2019 Miro Hrončok <mhroncok@redhat.com> - 31-14
- No longer obsolete python2-blockdiag (#1699834)

* Tue Apr 16 2019 Orion Poplawski <orion@nwra.com> - 31-13
- Obsolete python2-envisage (#1700310)

* Tue Apr 16 2019 Miro Hrončok <mhroncok@redhat.com> - 31-12
- Obsolete mongodb, mongodb-server, mongodb-test < 4.0.3-4 (#1700073)
- Obsolete python2-certbot < 0.31.0-3 and python2-josepy < 1.1.0-7 (#1700045)

* Mon Apr 15 2019 Kevin Fenzi <kevin@scrye.com> - 31-11
- Obsolete mongodb < 4.0.3-3 (#1700073)

* Mon Apr 15 2019 Miro Hrončok <mhroncok@redhat.com> - 31-10
- Obsolete python2-cinderclient < 3.5.0-2

* Sun Apr 14 2019 Miro Hrončok <mhroncok@redhat.com> - 31-9
- Obsolete python2-testify < 0.11.0-13

* Thu Apr 11 2019 Fabio Valentini <decathorpe@gmail.com> - 31-8
- Add obsoletes for appcenter* packages.

* Wed Apr 10 2019 Kalev Lember <klember@redhat.com> - 31-7
- Remove gnome-books obsoletes now that the package is back in Fedora (#1698489)

* Mon Apr 08 2019 Miro Hrončok <mhroncok@redhat.com> - 31-6
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Apr 04 2019 Miro Hrončok <mhroncok@redhat.com> - 31-5
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal
- Obsolete python2-pylint (#1686848)
- Obsolete python2 subpackages of ceph (#1687998)

* Thu Apr 04 2019 Kalev Lember <klember@redhat.com> - 31-4
- Obsolete PyXB (#1696209)

* Fri Mar 08 2019 Miro Hrončok <mhroncok@redhat.com> - 31-3
- Obsolete Python 2 Sphinx packages
  https://fedoraproject.org/wiki/Changes/Sphinx2

* Mon Mar 04 2019 Miro Hrončok <mhroncok@redhat.com> - 31-2
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Feb 22 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 31-1
- Cleaned up for F31.
- Obsolete empathy (bz 1680068).

* Tue Feb 19 2019 Pete Walter <pwalter@fedoraproject.org> - 30-28
- Bump librepo and libcomps python2 subpackage obsoletes versions

* Tue Feb 19 2019 Pete Walter <pwalter@fedoraproject.org> - 30-27
- Bump dnf python2 subpackage obsoletes versions

* Tue Feb 19 2019 Bastien Nocera <bnocera@redhat.com> - 30-26
- Obsolete gnome-books after split off from gnome-documents

* Wed Feb 13 2019 Björn Esser <besser82@fedoraproject.org> - 30-25
- Obsolete trafficserver < 5.3.0-14 and its sub-packages

* Tue Feb 12 2019 Kalev Lember <klember@redhat.com> - 30-24
- Obsolete python-xpyb-devel as well, in addition to python2-xpyb

* Tue Feb 12 2019 Kalev Lember <klember@redhat.com> - 30-23
- Obsolete vala-compat

* Mon Feb 11 2019 Kalev Lember <klember@redhat.com> - 30-22
- Obsolete python2-isort

* Fri Feb 08 2019 Kalev Lember <klember@redhat.com> - 30-21
- Obsolete wxGTK and its subpackages

* Thu Feb 07 2019 Miro Hrončok <mhroncok@redhat.com> - 30-20
- Obsolete another batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jan 31 2019 Pete Walter <pwalter@fedoraproject.org> - 30-19
- Obsolete python2-samba

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 30-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Pete Walter <pwalter@fedoraproject.org> - 30-17
- Obsolete python2-librepo

* Tue Jan 29 2019 Pete Walter <pwalter@fedoraproject.org> - 30-16
- Obsolete python2-bodhi and python2-bodhi-client
- Bump dnf-plugins-core python2 package obsoletes versions

* Thu Jan 10 2019 Kalev Lember <klember@redhat.com> - 30-15
- Obsolete gedit-plugin-dashboard

* Sat Jan 05 2019 Pete Walter <pwalter@fedoraproject.org> - 30-14
- Fix python2-blockdev and python2-dnf-plugins obsolete versions

* Thu Dec 13 2018 Miro Hrončok <mhroncok@redhat.com> - 30-13
- Obsolete sixth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 30-12
- Obsolete fifth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Nov 01 2018 Miro Hrončok <mhroncok@redhat.com> - 30-11
- Obsolete fourth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Oct 05 2018 Miro Hrončok <mhroncok@redhat.com> - 30-10
- Obsolete fourth batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Sep 30 2018 Miro Hrončok <mhroncok@redhat.com> - 30-9
- Obsolete third batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 30-8
- Obsolete second batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 18 2018 Miro Hrončok <mhroncok@redhat.com> - 30-7
- Obsolete python2-mapnik (#1630222)
- Obsolete first batch of problematic mass retired python2 packages
  https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 11 2018 Scott Talbert <swt@techie.net> - 30-6
- Obsolete python2-libconcord, python2-pyqtgraph, python2-pyopengl-tk

* Mon Sep 03 2018 Miro Hrončok <mhroncok@redhat.com> - 30-5
- Obsolete python2-behave (#1624838)

* Wed Aug 22 2018 Miro Hrončok <mhroncok@redhat.com>
- Obsolete more python3 packages (#1610422)

* Mon Aug 20 2018 Miro Hrončok <mhroncok@redhat.com> - 30-3
- Bump up version of abrt packages

* Fri Aug 17 2018 Miro Hrončok <mhroncok@redhat.com> - 30-2
- Obsolete python3-svgwrite (#1610422) (#1605936)

* Thu Aug 16 2018 Miro Hrončok <mhroncok@redhat.com> - 30-1
- Fedora 30 bump (removed all no longer needed obsoletes)

* Thu Aug 16 2018 Miro Hrončok <mhroncok@redhat.com> - 29-17
- Obsolete python3-trollius-redis (#1610422) (#1606877)

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 29-16
- Obsolete vte3 (#1315425)

* Wed Aug 08 2018 Miro Hrončok <mhroncok@redhat.com> - 29-15
- Obsolete python3-ovirt-register (#1610422) (#1605819)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 29-14
- Obsolete removed python3 packages (#1610422)

* Tue Jul 31 2018 Stephen Gallagher <sgallagh@redhat.com> - 29-13
- Obsolete rolekit

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 29-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Pete Walter <pwalter@fedoraproject.org> - 29-11
- Obsolete fedora-productimg-workstation
- Bump NetworkManager-glib and libnm-gtk obsoletes versions

* Wed Jun 06 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 29-10
- Add ppc64-utils (https://bugzilla.redhat.com/show_bug.cgi?id=1588130).

* Fri May 18 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 29-9
- Add abrt-related python2 packages.
- Clean up and add more documentation, since many provenpackagers are modifying
  this package without including the needed information.
- Remove the last F29 entries.
- Fix bogus date in %%changelog.

* Thu May 17 2018 Lubomir Rintel <lkundrak@v3.sk> - 29-8
- Bump version of libnm-glib packages to f28 updates

* Mon May 07 2018 Pete Walter <pwalter@fedoraproject.org> - 29-7
- Obsolete python2-caribou and python3-caribou as well (#1568670)

* Fri May  4 2018 Peter Robinson <pbrobinson@fedoraproject.org> 29-6
- Obsolete libmx and presence
- Obsolete clucene09-core xorg-x11-drv-freedreno

* Fri May 04 2018 Pete Walter <pwalter@fedoraproject.org> - 29-5
- Obsolete old caribou versions (#1568670)

* Tue Apr 24 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 29-4
- Remove a number of "Remove in F28" and "Remove in F29" entries.

* Mon Apr 23 2018 Lubomir Rintel <lkundrak@v3.sk> - 29-3
- Obsolete libnm-glib based packages

* Thu Apr 12 2018 Kalev Lember <klember@redhat.com> - 29-2
- Fix bind99 obsoletes versions, obsolete mozjs17-devel

* Thu Apr 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 29-1
- bind99, mozjs17, python2-zeroconf, python2-chromecast

* Wed Feb 07 2018 Kalev Lember <klember@redhat.com> - 28-2
- Add xulrunner obsoletes

* Mon Nov 13 2017 Pete Walter <pwalter@fedoraproject.org> - 28-1
- Obsolete compat-ImageMagick693, compat-libvpx1

* Wed Nov  8 2017 Peter Robinson <pbrobinson@fedoraproject.org> 27-10
- Obsolete  compat-gnutls28, libsilc, pam_pkcs11, python-dapp

* Fri Oct 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 27-9
- Obsoletes: kdegraphics-strigi-analyzer kfilemetadata
- bump libkexiv2 version

* Sat Oct 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 27-8
- Obsolets: kf5-libkface (#1423813)

* Sat Oct 07 2017 Rex Dieter <rdieter@fedoraproject.org> - 27-7
- Obsoletes: strigi, libkexiv2 (#1498850)

* Tue Aug 29 2017 Kalev Lember <klember@redhat.com> - 27-6
- Add seed obsoletes

* Tue Aug 29 2017 Kalev Lember <klember@redhat.com> - 27-5
- Add hawkey and libhif obsoletes

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Adam Williamson <awilliam@redhat.com> - 27-3
- Add webkitgtk and webkitgtk3 (and -devel) - RHBZ #1443614

* Wed Jun 21 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 27-2
- Add various devassistant-related packages from https://bugzilla.redhat.com/show_bug.cgi?id=1463408

* Tue May 16 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 27-1
- Add perl ZMQ packages from https://bugzilla.redhat.com/show_bug.cgi?id=1451372

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 14 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 26-1
- Initial release; nothing to obsolete yet.
