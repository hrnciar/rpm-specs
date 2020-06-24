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
Version:    33
Release:    14
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

    if pkg == '%1' then
        rpm.expand('%{error:No package name provided to obsolete}')
    end
    if ver == '%2' then
        rpm.expand('%{error:No version provided to obsolete}')
    end

    if not string.find(ver, '-') then
        rpm.expand('%{error:You must provide a version-release, not just a version.}')
    end

    local o = pkg .. ' < ' .. ver
    print('Obsoletes: ' .. o)

    -- Append this obsolete to the last set of obsoletes in the list
    local list = obs[#obs].list
    list[#list+1] = o
}

# Don't use this macro!  Only here because people keep doing this wrong.
%define obsolete_wrong() %{lua:
    local pkg = rpm.expand('%1')
    local ver = rpm.expand('%2')

    if pkg == '%1' then
        rpm.expand('%{error:No package name provided to obsolete}')
    end
    if ver == '%2' then
        rpm.expand('%{error:No version provided to obsolete}')
    end

    local o = pkg .. ' < ' .. ver
    print('Obsoletes: ' .. o)

    -- Append this obsolete to the last set of obsoletes in the list
    local list = obs[#obs].list
    list[#list+1] = o
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
            print('  ' .. obs[i].list[j] .. '\\n')
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
# Remove in F34
# %%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# %%obsolete foo 3.5-7

# ========================================
# Please place non-python2 Obsoletes: here
# ========================================

# Remove in F36
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1781359
%obsolete epiphany-runtime 1:3.36.0-2

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/aeskulap/c/eb0558f61370d8b08285159f887abea4a80334ed
%obsolete aeskulap 0.2.2-0.38

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/compat-gnutls28/c/38836d77d1306de68ea3a4e51a0d02459b1250de
%obsolete compat-gnutls28 3.3.21-2

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/libsilc/c/dd3a86f50d6a31111d0c40897d6e3784e696ffb9
%obsolete libsilc 1.1.10-16
%obsolete libsilc-devel 1.1.10-16
%obsolete libsilc-doc 1.1.10-16

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/pam_pkcs11/c/f88c608e75b9c886efd15317feae806fa620346b
%obsolete pam_pkcs11 0.6.8-9

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/gstreamer/c/716318ed1f6195efe3698e2f268ec4fc18c433bb
# gstreamer
%obsolete gstreamer 0.10.36-27
%obsolete gstreamer-devel 0.10.36-27
%obsolete gstreamer-devel-docs 0.10.36-27
%obsolete gstreamer-tools 0.10.36-27
# gstreamer-plugins-bad-free
%obsolete gstreamer-plugins-bad-free 0.10.23-51
%obsolete gstreamer-plugins-bad-free-devel 0.10.23-51
%obsolete gstreamer-plugins-bad-free-devel-docs 0.10.23-51
%obsolete gstreamer-plugins-bad-free-extras 0.10.23-51
# gstreamer-plugins-base
%obsolete gstreamer-plugins-base-devel-docs 0.10.36-27
%obsolete gstreamer-plugins-base 0.10.36-27
%obsolete gstreamer-plugins-base-devel 0.10.36-27
%obsolete gstreamer-plugins-base-tools 0.10.36-27
# gstreamer-plugins-good
%obsolete gstreamer-plugins-good-devel-docs 0.10.31-25
%obsolete gstreamer-plugins-good 0.10.31-25
%obsolete gstreamer-plugins-good-extras 0.10.31-25
# gstreamer-python
%obsolete gstreamer-python-devel 0.10.22-22

# Remove in F34
%obsolete_ticket https://src.fedoraproject.org/rpms/farstream/c/1725984c6844b54eabc897120b87bd32d00c3525
%obsolete farstream 0.1.2-14
%obsolete farstream-devel 0.1.2-14
%obsolete farstream-python 0.1.2-14

# Remove in F34
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1813401
%obsolete gradle 4.4.1-5

# Remove in F34
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1827417
%obsolete mod_auth_kerb 5.4-34

# ==========================================
# Please collect the python 3.7 Obsoletes: here
# ==========================================

# Remove in F34
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1754151
%obsolete antimony 0.9.3-15
%obsolete atomic 1.22.1-29
%obsolete atomic-registries 1.22.1-29
%obsolete authconfig 7.0.1-9
%obsolete dreampie-python3 1.1.1-18
%obsolete elastic-curator 4.2.5-7
%obsolete fedora-productimg-cloud 26-5
%obsolete gcc-python3-debug-plugin 0.17-5
%obsolete gcc-python3-plugin 0.17-5
%obsolete gfal2-python3 1.9.5-4
%obsolete gnome-dvb-daemon 0.2.91-0.13
%obsolete graphite-api 1.1.3-15
%obsolete graphite-web 1.1.5-3
%obsolete greenwave 0.9.4-3
%obsolete json_diff 1.5.0-2
%obsolete kaadbg 0.3.0-12
%obsolete lorem-ipsum-generator 0.3.20161122git-25
%obsolete menulibre 2.2.1-3
%obsolete mkdocs-bootswatch 0.5.0-4
%obsolete nodepool-driver-openstack 3.0.0-6
%obsolete nodepool-driver-static 3.0.0-6
%obsolete pintail 0.4-9
%obsolete python-aiorpcx 0.10.5-2
%obsolete python-sphinx-autobuild 0.7.1-14
%obsolete python3-Lektor 3.0.1-8
%obsolete python3-ahkab 0.18-15
%obsolete python3-alchimia 0.7.0-7
%obsolete python3-backports-unittest_mock 1.2.1-8
%obsolete python3-backports_abc 0.5-10
%obsolete python3-bash8 0.1.1-19
%obsolete python3-bitlyapi 0.1.1-21
%obsolete python3-blockdiag-devel 1.5.4-7
%obsolete python3-bodhi3 3.14.0-2
%obsolete python3-bodhi3-client 3.14.0-2
%obsolete python3-bz2file 0.98-10
%obsolete python3-cassandra-driver 3.19.0-2
%obsolete python3-castellan 0.5.0-8
%obsolete python3-cattrs 0.9.0-4
%obsolete python3-ceilometermiddleware 0.5.0-8
%obsolete python3-cookies 2.2.1-16
%obsolete python3-couchdb 1.0-15
%obsolete python3-curses_ex 0.3-12
%obsolete python3-cursive 0.1.2-9
%obsolete python3-deltasigma 0.2-17
%obsolete python3-django-avatar 4.1.0-5
%obsolete python3-django-countries 5.3.1-3
%obsolete python3-django-jsonfield 2.0.2-9
%obsolete python3-django-notifications-hq 1.5.0-3
%obsolete python3-django-rest-framework-composed-permissions 0.1-10
%obsolete python3-django-stopforumspam 1.8-8
%obsolete python3-django-tinymce 2.4.0-11
%obsolete python3-dlib 19.4-11
%obsolete python3-dpm 1.13.0-2
%obsolete python3-epdb 0.15-10
%obsolete python3-fabric 2.0.0-8
%obsolete python3-fabric3 1.13.1-9
%obsolete python3-fabulous 0.3.0-11
%obsolete python3-fb303 0.10.0-20
%obsolete python3-flask-classy 0.6.10-12
%obsolete python3-flask-debugtoolbar 0.10.0-14
%obsolete python3-flickrapi 2.2.1-10
%obsolete python3-flup 1.0.3-2
%obsolete python3-forensic1394 0.2-24
%obsolete python3-fsmonitor 0.1-18
%obsolete python3-gflags 2.0-18
%obsolete python3-gfm 0.1.3-12
%obsolete python3-google-apputils 0.4.2-17
%obsolete python3-googletrans 2.2.0-8
%obsolete python3-grafyaml 0.0.5-13
%obsolete python3-grapefruit 0.1a4-11
%obsolete python3-hardware 0.18-13
%obsolete python3-honcho 1.0.1-4
%obsolete python3-http-parser 0.8.3-22
%obsolete python3-httpwatcher 0.5.2-3
%obsolete python3-importlib-metadata 0.23-2
%obsolete python3-inifile 0.3-15
%obsolete python3-jenkinsapi 0.2.29-12
%obsolete python3-k8sclient 0.3.0-11
%obsolete python3-kafka 1.4.3-4
%obsolete python3-keystonemiddleware 4.21.0-3
%obsolete python3-lfc 1.13.0-2
%obsolete python3-marrow-mailer 4.0.2-12
%obsolete python3-marrow-util 1.2.3-11
%obsolete python3-microversion-parse 0.1.3-12
%obsolete python3-module-build-service-copr 0.4-6
%obsolete python3-mongoengine 0.18.2-2
%obsolete python3-netlib 0.16-3
%obsolete python3-ngram 3.3.2-3
%obsolete python3-nineml 1.0.1-3
%obsolete python3-nose-ignore-docstring 0.2-6
%obsolete python3-nose-parameterized 0.6.0-3
%obsolete python3-offtrac 0.1.0-20
%obsolete python3-os-win 2.2.0-10
%obsolete python3-oslo-cache 1.28.0-4
%obsolete python3-oslo-cache-tests 1.28.0-4
%obsolete python3-oslo-messaging 8.1.2-2
%obsolete python3-oslo-messaging-tests 8.1.2-2
%obsolete python3-oslo-middleware 3.34.0-3
%obsolete python3-oslo-middleware-tests 3.34.0-3
%obsolete python3-oslo-policy 1.33.2-4
%obsolete python3-oslo-policy-tests 1.33.2-4
%obsolete python3-oslo-privsep 1.13.0-10
%obsolete python3-oslo-privsep-tests 1.13.0-10
%obsolete python3-oslo-reports 1.26.0-4
%obsolete python3-oslo-reports-tests 1.26.0-4
%obsolete python3-oslo-rootwrap 5.13.0-4
%obsolete python3-oslo-rootwrap-tests 5.13.0-4
%obsolete python3-oslo-service 1.29.0-4
%obsolete python3-oslo-service-tests 1.29.0-4
%obsolete python3-oslo-vmware 2.26.0-4
%obsolete python3-oslo-vmware-tests 2.26.0-4
%obsolete python3-osprofiler 1.11.0-8
%obsolete python3-pankoclient 0.3.0-10
%obsolete python3-pankoclient-tests 0.3.0-10
%obsolete python3-pep8 1.7.1-5
%obsolete python3-pg8000 1.12.3-3
%obsolete python3-port-for 0.4-9
%obsolete python3-publicsuffix 1.1.0-10
%obsolete python3-pybloomfiltermmap 0.3.15-15
%obsolete python3-pycadf 2.4.0-11
%obsolete python3-pycscope 1.2.1-20
%obsolete python3-pyftpdlib 1.5.4-9
%obsolete python3-pyjf3 0.3-13
%obsolete python3-pykalman 0.9.5-25
%obsolete python3-pykde4 4.14.3-31
%obsolete python3-pypump 0.6-14
%obsolete python3-pyside 1.2.4-11
%obsolete python3-pystache 0.5.4-13
%obsolete python3-pyswip 0.2.7-6
%obsolete python3-pytest-pep8 1.0.6-22
%obsolete python3-qscintilla 2.11.2-5
%obsolete python3-rauth 0.7.3-8
%obsolete python3-releases 1.6.0-6
%obsolete python3-restauth 0.6.1-20
%obsolete python3-restauth-common 0.6.2-19
%obsolete python3-ripe-atlas-cousteau 1.3-11
%obsolete python3-ripe-atlas-sagan 1.1.11-12
%obsolete python3-ripozo 1.3.0-13
%obsolete python3-sanic 0.8.0-3
%obsolete python3-scandir 1.9.0-7
%obsolete python3-seesaw 0.10.0-7
%obsolete python3-shogun 6.0.0-16
%obsolete python3-slack_cleaner 0.6.0-2
%obsolete python3-socketIO-client 0.7.2-5
%obsolete python3-socketpool 0.5.3-16
%obsolete python3-stestr-sql 2.4.0-3
%obsolete python3-subunit2sql 1.9.0-4
%obsolete python3-subunit2sql-graph 1.9.0-4
%obsolete python3-tbgrep 0.3.0-18
%obsolete python3-thriftpy 0.3.9-11
%obsolete python3-tpg 3.2.2-10
%obsolete python3-traceback2 1.4.0-21
%obsolete python3-tw2-jqplugins-ui 2.3.0-9
%obsolete python3-tw2-jquery 2.2.0.2-11
%obsolete python3-units 0.07-8
%obsolete python3-vips 8.7.4-3
%obsolete python3-virtkey 0.63.0-13
%obsolete python3-windtalker 0.0.4-11
%obsolete python3-yubikey-piv-manager 1.4.2-9
%obsolete python3-zc-buildout 2.5.3-12
%obsolete python3-zipp 0.5.1-3
%obsolete python3-zookeeper 3.4.9-14
%obsolete python3-zope-contenttype 4.1.0-15
%obsolete python3-zope-datetime 4.1.0-13
%obsolete python3-zope-dottedname 4.1.0-16
%obsolete python3-zope-filerepresentation 4.1.0-15
%obsolete python3-zope-i18n 4.1.0-14
%obsolete python3-zope-processlifetime 2.1.0-11
%obsolete python3-zope-proxy 4.2.0-10
%obsolete python3-zope-sequencesort 4.0.1-13
%obsolete pythonqt 3.2-21
%obsolete ripe-atlas-tools 2.0.2-9
%obsolete shiboken-python3-libs 1.2.4-15
%obsolete vault 0.0.3-4
%obsolete vint 0.3.18-4

# Remove in F35
# obsolete_ticket continues form previous section
%obsolete python3-traceback2 1.4.0-21


# ==========================================
# Please collect the python2 Obsoletes: here
# ==========================================

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1578359

# Python 2 packages removed in Fedora 15 but never obsoleted
%obsolete OpenIPMI-gui 2.0.18-5
%obsolete cel 1.2-10
%obsolete crystalspace 1.2.1-9
%obsolete crystalspace-devel 1.2.1-9
%obsolete fedora-devshell 0.1.1-5
%obsolete genesis 0.4.3-4
%obsolete gmixer 1.3-22
%obsolete gsh 0.3-11
%obsolete jokosher 1.0-0.13
%obsolete libchamplain-python 0.6.1-5
%obsolete lybniz 1.3.2-7
%obsolete mediascrapper 0.1-8
%obsolete museek+-bindings 0.3-0.4
%obsolete museek+-mucous 0.3-0.4
%obsolete museek+-murmur 0.3-0.4
%obsolete nagios-plugins-rhev 1.0.0-3
%obsolete pybackpack 0.5.7-5
%obsolete pytc 0.8-6
%obsolete python-argparse 1.1-3
%obsolete python-cly 0.9-4
%obsolete python-goopy 0.1-10
%obsolete python-hash_ring 1.2-5
%obsolete python-id3 1.2-17
%obsolete python-transitfeed 1.1.9-8
%obsolete python-twyt 0.9.2-5
%obsolete pytyrant 1.1.17-4
%obsolete transbot 0.2-8

# Python 2 packages removed in Fedora 16 but never obsoleted
%obsolete Miro 3.5.1-2
%obsolete aldrin 0.13-7
%obsolete bittorrent 4.4.0-17
%obsolete cnetworkmanager 0.21.1-4
%obsolete ethos-python 0.2.2-12
%obsolete gbirthday 0.6.5-4
%obsolete gnome-python2-brasero 2.32.0-2
%obsolete gnome-python2-evince 2.32.0-2
%obsolete gquilt 0.25-2
%obsolete gtraffic 1.01-7
%obsolete healpy 0.9.6.1-7
%obsolete kdeedu 4.6.5-2
%obsolete kdeedu-math 4.6.5-2
%obsolete liblicense-python 0.8.1-6
%obsolete moovida-base 1.0.9-5
%obsolete moovida-plugins-bad 1.0.9-5
%obsolete moovida-plugins-good 1.0.9-5
%obsolete mumbles 0.4-15
%obsolete pigment-python 0.3.12-5
%obsolete presto-utils 0.3.4-6
%obsolete pytagger 0.5-7
%obsolete python-Chaco 3.3.1-4
%obsolete python-Enable 3.3.1-3
%obsolete python-TraitsBackendWX 3.4.0-5
%obsolete python-mechanoid 0.6.9-15
%obsolete python-pygooglechart 0.2.1-8
%obsolete python-rabbyt 0.8.3-4
%obsolete python-tilecache 2.11-7
%obsolete pyxmms 2.06-14
%obsolete pyzzub 0.2.6-15
%obsolete qtiplot 0.9.8.3-2
%obsolete referencer 1.1.6-16
%obsolete scribes 0.3.3.3-8
%obsolete seedit 2.2.0-9
%obsolete seedit-gui 2.2.0-9
%obsolete straw 0.27-20
%obsolete tinyerp 4.2.3.4-8
%obsolete tinyerp-server 4.2.3.4-8
%obsolete trytond-google-translate 1.8.0-5

# Python 2 packages removed in Fedora 17 but never obsoleted
%obsolete antlr3-python 3.1.2-15
%obsolete avant-window-navigator 0.4.1-0.5
%obsolete awn-extras-applets 0.4.2-0.7
%obsolete fusion-icon-qt 0.1.0-0.11
%obsolete gestikk 0.6.1-8
%obsolete gget 0.0.4-17
%obsolete hulahop 0.7.1-4
%obsolete itaka 0.2.2-4
%obsolete luci 0.25.0-2
%obsolete openstack-keystone 2011.3.1-4
%obsolete pida 0.5.1-14
%obsolete puritan 0.4-8
%obsolete pyactivemq 0.1.0-14
%obsolete pyevent 0.3-10
%obsolete pyjamas-desktop 0.7-8
%obsolete python-assets 0.1.1-5
%obsolete python-desktop-agnostic 0.3.92-2
%obsolete python-libgmail 0.1.11-6
%obsolete python-mako0.4 0.4.2-8
%obsolete python-numarray 1.5.2-11
%obsolete python-sqlite2 1:2.3.5-5
%obsolete python-text_table 0.02-6
%obsolete python-wehjit 0.2.2-5
%obsolete pyxf86config 0.3.37-11
%obsolete qedje-python 0.4.0-10
%obsolete qzion-python 0.4.0-12
%obsolete rainbow 0.8.6-4
%obsolete telepathy-sunshine 0.2.0-3

# Python 2 packages removed in Fedora 18 but never obsoleted
%obsolete Django-south 0.7.5-2
%obsolete PyAmanith 0.3.35-13
%obsolete autokey 0.81.4-2
%obsolete blogtk 2.0-8
%obsolete boost141-python 1.41.0-3
%obsolete django-tinymce 1.5-4
%obsolete docky 2.0.12-4
%obsolete hamster-applet 2.32.1-4
%obsolete input-pad-python 1.0.1-5
%obsolete mod_python 3.3.1-19
%obsolete mod_scgi 1.13-6
%obsolete moksha 0.5.0-6
%obsolete natus-python 0.1.5-3
%obsolete ntfs-config 1.0.1-14
%obsolete openchange-python 1.0-11
%obsolete openstack-nova-compute 2012.1.3-4
%obsolete openstack-nova-network 2012.1.3-4
%obsolete openstack-nova-volume 2012.1.3-4
%obsolete ovirt-engine-log-collector 3.0.0.0001-16
%obsolete pacemaker-cloud 0.5.0-3
%obsolete pyfuzzy 0.1.0-5
%obsolete python-cement-devtools 0.8.18-3
%obsolete python-exo 0.6.2-5
%obsolete python-keystone-auth-token 2012.1.3-4
%obsolete python-modjkapi 0.1.2.28-8
%obsolete python-natus 0.1.5-3
%obsolete python-nose1.1 1.1.2-6
%obsolete typepad-motion 1.1.3-5
%obsolete xulrunner-python 2.0-2

# Python 2 packages removed in Fedora 19 but never obsoleted
%obsolete HippoDraw-python 1.21.3-7
%obsolete bootchart 0.14.0-4
%obsolete canto 0.7.4-6
%obsolete comoonics-base-py 0.1-8
%obsolete comoonics-cdsl-py 0.2-21
%obsolete comoonics-cluster-py 0.1-27
%obsolete django-annoying 0.7.6-4
%obsolete django-avatar 2.0a1-7
%obsolete glusterfs-swift 3.3.1-4
%obsolete glusterfs-swift-account 3.3.1-4
%obsolete glusterfs-swift-container 3.3.1-4
%obsolete glusterfs-swift-object 3.3.1-4
%obsolete glusterfs-swift-plugin 3.3.1-4
%obsolete glusterfs-swift-proxy 3.3.1-4
%obsolete gnome-lirc-properties 0.5.1-5
%obsolete matahari-lib 0.6.0-4
%obsolete matahari-python 0.6.0-4
%obsolete matahari-rpc 0.6.0-4
%obsolete matahari-shell 0.6.0-4
%obsolete obapps 0.1.7-4
%obsolete openstack-swift-object 1.7.4-2
%obsolete python-TraitsGUI 3.5.0-5
%obsolete python-drizzle 0.08.2-10
%obsolete python-nufw 2.4.3-7
%obsolete python-quixote 2.4-16
%obsolete python-sqlalchemy0.7 0.7.3-8
%obsolete syck-python 0.61-18
%obsolete trac-agilo-plugin 0.9.7-4
%obsolete util-vserver-python 0.30.215+svn2929-1604

# Python 2 packages removed in Fedora 20 but never obsoleted
%obsolete PythonCAD 0.1.37-5
%obsolete aeolus-audrey-agent 0.5.1-3
%obsolete autobuild-applet 1.0.3-17
%obsolete btparser-python 0.26-2
%obsolete django-tables 0.3-0.6
%obsolete firmware-extract 2.0.13-5
%obsolete firstaidkit-engine 0.3.2-7
%obsolete firstboot 19.2-2
%obsolete fpaste-server 0.2-2
%obsolete gazpacho 0.7.2-14
%obsolete gnome-specimen 0.4-7
%obsolete ibus-panel-extensions-python 1.4.99.20111207-7
%obsolete libbtctl 0.11.1-14
%obsolete libprelude-python 1:1.0.0-18
%obsolete libpreludedb-python 1:1.0.0-17
%obsolete metagoofil 1.4b-8
%obsolete mysql-workbench 5.2.47-3
%obsolete openstack-swift-account 1.8.0-4
%obsolete openstack-tempo 0-0.4
%obsolete prelude-notify 0.9-0.11
%obsolete python-EnthoughtBase 3.0.6-6
%obsolete python-EnvisageCore 3.1.3-6
%obsolete python-EnvisagePlugins 3.1.3-6
%obsolete python-TraitsBackendQt 3.5.0-6
%obsolete python-arm4 1.2-8
%obsolete python-django-lint 0.13-16
%obsolete python-iguanaIR 1.0.3-3
%obsolete python-nova-adminclient 0.1.8-5
%obsolete python-psycopg 1.1.21-19
%obsolete python-quantumclient 2:2.2.1-4
%obsolete python-setupdocs 1.0.5-6
%obsolete python-transifex 0.1.7-3
%obsolete rhevsh 1.0-2
%obsolete smart 1.3.1-69
%obsolete smart-gui 1.3.1-69
%obsolete ufl-python 0.1-0.4
%obsolete zyx-liveinstaller 0.2.4-7

# Python 2 packages removed in Fedora 21 but never obsoleted
%obsolete SOAPpy 0.11.6-18
%obsolete askbot 0.7.48-12
%obsolete bcfg2-web 1.3.2-3
%obsolete bzr-explorer 1.3.0-2
%obsolete cinepaint 1.3-10
%obsolete comedilib-devel 0.8.1-13
%obsolete condor-bosco 8.1.1-0.4
%obsolete django-recaptcha 0.1-6
%obsolete django-sct 0.6-6
%obsolete eucalyptus-console 3.3.0-0.6
%obsolete funnel 0.0-6
%obsolete gausssum 2.2.6-3
%obsolete gnome-shell-search-fedora-packages 1.1.2-4
%obsolete gnome-shell-search-github-repositories 1.0.2-4
%obsolete gnome-shell-search-pinboard 1.0.3-4
%obsolete heat 7-5
%obsolete heat-jeos 9-3
%obsolete hotot-gtk 0.9.9-8
%obsolete ice-python 3.5.1-3
%obsolete input-pad-pygobject2 1.0.2-6
%obsolete katello-cli-common 1.3.5-3
%obsolete lastuser 0.1-6
%obsolete libbeagle-python 0.3.9-12
%obsolete libimobiledevice-python 1.1.5-4
%obsolete metakit 2.4.9.7-15
%obsolete openslides 1.3.1-3
%obsolete openstack-neutron-bigswitch 2013.2-2
%obsolete openstack-neutron-brocade 2013.2-2
%obsolete openstack-neutron-cisco 2013.2-2
%obsolete openstack-neutron-hyperv 2013.2-2
%obsolete openstack-neutron-linuxbridge 2013.2-2
%obsolete openstack-neutron-mellanox 2013.2-2
%obsolete openstack-neutron-metaplugin 2013.2-2
%obsolete openstack-neutron-midonet 2013.2-2
%obsolete openstack-neutron-ml2 2013.2-2
%obsolete openstack-neutron-nec 2013.2-2
%obsolete openstack-neutron-openvswitch 2013.2-2
%obsolete openstack-neutron-plumgrid 2013.2-2
%obsolete openstack-neutron-ryu 2013.2-2
%obsolete openstack-savanna 2014.1.b2-4
%obsolete picviz 0.6-13
%obsolete picviz-gui 0.6-13
%obsolete pootle 2.1.6-8
%obsolete postr 0.12.4-10
%obsolete python-ZooKeeper 3.4.5-13
%obsolete python-askbot-fedmsg 0.1.1-2
%obsolete python-authhub 0.1.2-4
%obsolete python-coffin 0.3.7-3
%obsolete python-django-addons 0.6.6-2
%obsolete python-django-authopenid 1.0.1-8
%obsolete python-django-longerusername 0.4-5
%obsolete python-django14 1.4.20-2
%obsolete python-django15 1.5.9-2
%obsolete python-eucadmin 3.3.0-0.6
%obsolete python-jinja 1.2-11
%obsolete python-lamson 1.3.4-2
%obsolete python-paver 1.2.1-3
%obsolete python-ssh 1.7.14-4
%obsolete python-webdav-library 0.3.0-7
%obsolete pytrainer 1.9.1-6
%obsolete pywcs 1.11-5
%obsolete qbzr 0.23.1-2
%obsolete s3ql 1.13.2-2
%obsolete semantik 0.9.1-2
%obsolete sfbm 0.7-2
%obsolete spacewalk-backend 2.0.3-3
%obsolete spacewalk-backend-config-files-common 2.0.3-3
%obsolete spacewalk-backend-iss-export 2.0.3-3
%obsolete spacewalk-backend-libs 2.0.3-3
%obsolete spacewalk-backend-server 2.0.3-3
%obsolete spacewalk-backend-sql 2.0.3-3
%obsolete spacewalk-backend-sql-postgresql 2.0.3-3
%obsolete spacewalk-backend-tools 2.0.3-3
%obsolete spacewalk-backend-xml-export-libs 2.0.3-3
%obsolete spacewalk-backend-xmlrpc 2.0.3-3
%obsolete spectrum 1.4.8-13
%obsolete sugar-tamtam-common 0-0.13
%obsolete transifex 1.2.1-12
%obsolete xesam-tools 0.6.1-11

# Python 2 packages removed in Fedora 22 but never obsoleted
%obsolete ReviewBoard 2.0.18-2
%obsolete apt-python 0.5.15lorg3.95-10
%obsolete bro 1.5.1-13
%obsolete cnucnu 0-0.18
%obsolete gfal-python 1.16.0-6
%obsolete identicurse 0.8.2-7
%obsolete kate-pate 4.14.3-7
%obsolete lcg-util-python 1.16.0-5
%obsolete mosquitto-python 1.3.5-2
%obsolete nifti2dicom 0.4.9-2
%obsolete openlmi-software 0.5.0-6
%obsolete ovirt-node 3.0.0-12
%obsolete ovirt-node-plugin-cim 3.0.0-12
%obsolete ovirt-node-plugin-puppet 3.0.0-12
%obsolete ovirt-node-plugin-snmp 3.0.0-12
%obsolete pympdtouchgui 0.327-8
%obsolete python-MAPI 7.1.14-2
%obsolete python-asyncmongo 0.1.3-7
%obsolete python-djblets 0.8.21-2
%obsolete python-gofer-amqplib 2.0.0-2
%obsolete python-migrate0.5 0.5.4-8
%obsolete python-setuptools_trial 0.5.12-8
%obsolete python-sqlalchemy0.5 0.5.8-12
%obsolete python-sqlamp 0.5.2-10
%obsolete python-tvrage 0.4.1-6
%obsolete python-wallaby 0.16.4-4
%obsolete python-wallabyclient 5.0.3-7
%obsolete python-xkit 0.4.2.2-7
%obsolete python-zfec 1.4.22-7
%obsolete sabayon 2.30.1-12
%obsolete sabayon-apply 2.30.1-12
%obsolete spambayes 1.1-0.11
%obsolete vdsm-reg 4.14.8.1-2
%obsolete zarafa-dagent 7.1.14-2
%obsolete zarafa-spooler 7.1.14-2

# Python 2 packages removed in Fedora 23 but never obsoleted
%obsolete ScientificPython 2.8-21
%obsolete ScientificPython-qt 2.8-21
%obsolete ScientificPython-tk 2.8-21
%obsolete at-spi-python 1.32.0-15
%obsolete bcfg2 1.3.3-6
%obsolete bcfg2-server 1.3.3-6
%obsolete ekg 1.8-0.18
%obsolete ekg2-python 0.3.1-15
%obsolete fedora-productimg-server 22-8
%obsolete font-manager 0.5.7-11
%obsolete gwibber 1:3.4.2-15
%obsolete ipsilon-authkrb 0.4.0-2
%obsolete ipsilon-tools 0.4.0-2
%obsolete istanbul 0.2.2-23
%obsolete openstack-sahara 2014.2.4-2
%obsolete pyjigdo 0.4.0.3-9
%obsolete python-Fiona 1.5.1-2
%obsolete python-async 0.6.1-10
%obsolete python-django-evolution 1:0.7.3-2
%obsolete python-django-memcached-pool 0.4.1-5
%obsolete python-django-piston 0.2.3-10
%obsolete python-fiat 1.5.0-2
%obsolete python-pbs 4.3.3-9
%obsolete python-rfc6266 0.0.4-5
%obsolete python-sgutils 0.2.1-7
%obsolete python-tgexpandingformwidget 0.1.3-16
%obsolete python-umemcache 1.6.3-4
%obsolete snake-server 0.11.1-6
%obsolete vdsm-python-zombiereaper 4.16.20-3

# Python 2 packages removed in Fedora 24 but never obsoleted
%obsolete ProDy 1.6.1-2
%obsolete ahc-tools 0.2.0-2
%obsolete ansible1.9 1.9.6-3
%obsolete autotest-framework-server 0.16.2-3
%obsolete bitbake 1.17.0-3
%obsolete cvs2commons 2.3.0-0.12
%obsolete dexter 0.18-11
%obsolete emesene 2.11.11-9
%obsolete fife 2:0.3.3r3-17
%obsolete frepple 2.1-4
%obsolete ghmm 0.7-13
%obsolete idjc 0.8.7-10
%obsolete imagefactory-plugins-Nova 1.1.7-3
%obsolete imagefactory-plugins-OpenStack 1.1.9-2
%obsolete imagefactory-plugins-Rackspace 1.1.9-2
%obsolete libixion-python 0.9.1-7
%obsolete listen 0.6.5-15
%obsolete lshell 0.9.16-6
%obsolete mitter 0.4.5-10
%obsolete openstack-heat-common 2015.1.3-2
%obsolete openstack-heat-gbp 2015.1.1-2
%obsolete openstack-ironic-common 2015.1.3-2
%obsolete openstack-manila-ui 1.0.1-2
%obsolete openstack-marconi 2014.1-4
%obsolete openstack-neutron-gbp 2015.1.1-2
%obsolete openstack-neutron-nuage 2015.1.3-2
%obsolete openstack-packstack 2015.1-0.12
%obsolete openstack-sahara-common 2015.1.3-2
%obsolete openstack-swift 2.3.0-4
%obsolete openstack-swift-container 2.3.0-4
%obsolete openstack-swift-plugin-swift3 1.9-2
%obsolete openstack-swift-proxy 2.3.0-4
%obsolete openstack-tripleo-heat-templates 0.7.9-14
%obsolete openstack-tuskar 0.4.15-4
%obsolete openstack-tuskar-ui 0.2.0-6
%obsolete openstack-zaqar 2015.1.0-3
%obsolete papyon 0.5.6-9
%obsolete pyliblo 0.9.1-11
%obsolete pymetar 0.14-14
%obsolete pystatgrab 0.5-17
%obsolete python-Coherence 0.6.6.2-11
%obsolete python-bcdoc 0.12.2-5
%obsolete python-ceilometer 2015.1.3-2
%obsolete python-cinder 2015.1.3-2
%obsolete python-designate 2015.1.0-3
%obsolete python-designate-tests 2015.1.0-3
%obsolete python-desktopcouch 1.0.8-4
%obsolete python-django-celery 3.1.9-3
%obsolete python-django-horizon 2015.1.4-2
%obsolete python-django-horizon-gbp 2015.1.1-3
%obsolete python-django-mako 0.1.5-0.6
%obsolete python-django-sahara 2014.2-0.4
%obsolete python-docker-registry-core 2.0.3-3
%obsolete python-dotconf 0.2.1-20
%obsolete python-espeak 0.5-12
%obsolete python-fife 2:0.3.3r3-17
%obsolete python-flask-mongoengine 0.7.1-3
%obsolete python-flask-testing 0.4.1-4
%obsolete python-gbpclient 0.10.1-2
%obsolete python-geoclue 0.1.0-9
%obsolete python-glance 2015.1.3-2
%obsolete python-gnash 1:0.8.10-20
%obsolete python-gnocchi 1.0.0-3
%obsolete python-hcs_utils 1.1.1-11
%obsolete python-ironic-discoverd 1.1.1-2
%obsolete python-javaobj 0-0.7
%obsolete python-keystone 2015.1.3-2
%obsolete python-lazy 1.2-6
%obsolete python-louie 1.1-17
%obsolete python-manila 2015.1.0-5
%obsolete python-neutron 2015.1.3-2
%obsolete python-neutron-tests 2015.1.3-2
%obsolete python-nevow 0.10.0-12
%obsolete python-nova 2015.1.3-2
%obsolete python-ogg 1.3-24
%obsolete python-rpi-gpio 0.5.11-2
%obsolete python-storm 0.20-6
%obsolete python-storm-django 0.20-6
%obsolete python-storm-mysql 0.20-6
%obsolete python-storm-postgresql 0.20-6
%obsolete python-storm-twisted 0.20-6
%obsolete python-storm-zope 0.20-6
%obsolete python-sybase 0.39-17
%obsolete python-tag 2013.1-14
%obsolete python-trove 2015.1.0-6
%obsolete python-tunepimp 0.5.3-29
%obsolete python-twill 0.9-14
%obsolete python-ufc 2.1.0-14
%obsolete python-vcpx 0.9.35-19
%obsolete python-vorbis 1.5-0.18
%obsolete python-wikimarkup 1.01-15
%obsolete python-wsme 0.6-5
%obsolete python2-wsme 0.7.0-3
%obsolete revisor-cli 2.2-12
%obsolete revisor-cobbler 2.2-12
%obsolete revisor-gui 2.2-12
%obsolete revisor-isolinux 2.2-12
%obsolete revisor-mock 2.2-12
%obsolete revisor-reuseinstaller 2.2-12
%obsolete rpm-compare-req 0.1.0-7
%obsolete sonata 1.6.2.1-16
%obsolete trac-peerreview-plugin 0.11-12
%obsolete undertaker 1.6.1-8
%obsolete upnp-inspector 0.2.2-12
%obsolete willie 4.5.0-3

# Python 2 packages removed in Fedora 25 but never obsoleted
%obsolete APLpy 1.0-5
%obsolete adonthell 0.3.5-8
%obsolete be 1.1.1-7
%obsolete gtkwhiteboard 1.3-12
%obsolete ino 0.3.6-5
%obsolete instack 0.0.6-3
%obsolete luma 3.0.7-7
%obsolete neso 2.6.0-7
%obsolete nf3d 0.8-6
%obsolete openlmi-pcp 0.6.0-5
%obsolete openlmi-python-base 0.6.0-5
%obsolete openlmi-python-providers 0.6.0-5
%obsolete openlmi-python-test 0.6.0-5
%obsolete openlmi-scripts-account 0.4.0-5
%obsolete openlmi-scripts-hardware 0.4.0-5
%obsolete openlmi-scripts-journald 0.4.0-5
%obsolete openlmi-scripts-locale 0.4.0-5
%obsolete openlmi-scripts-logicalfile 0.4.0-5
%obsolete openlmi-scripts-networking 0.4.0-5
%obsolete openlmi-scripts-powermanagement 0.4.0-5
%obsolete openlmi-scripts-realmd 0.4.0-5
%obsolete openlmi-scripts-selinux 0.4.0-5
%obsolete openlmi-scripts-service 0.4.0-5
%obsolete openlmi-scripts-software 0.4.0-5
%obsolete openlmi-scripts-sssd 0.4.0-5
%obsolete openlmi-scripts-storage 0.4.0-5
%obsolete openlmi-scripts-system 0.4.0-5
%obsolete openlmi-storage 0.8.1-4
%obsolete openlmi-tools 0.10.5-3
%obsolete orbited 0.7.10-15
%obsolete os-cloud-config 0.2.10-4
%obsolete pycolumnize 0.3.8-3
%obsolete pydb 1.26-15
%obsolete pyftpdlib 1.4.0-7
%obsolete pymol-wxpython 1.8-4
%obsolete pypop 0.7.0-17
%obsolete python-django-secure 1.0-5
%obsolete python-frappe-bench 0.92-5
%obsolete python-frappe-libs 5.3.0-4
%obsolete python-geoip-geolite2 2015.0303-7
%obsolete python-grib_api 1.14.5-3
%obsolete python-nikola 7.6.4-3
%obsolete python-slimit 0.8.1-4
%obsolete python-sqlalchemy-traversal 0.4.1-7
%obsolete python-tempest-lib 0.11.0-3
%obsolete python-tgscheduler 1.7.0-3
%obsolete python-tuskarclient 0.1.16-4
%obsolete python-visual 5.74-18
%obsolete python2-entry_point_inspector 0.1-4
%obsolete python2-espeak 0.5-15
%obsolete python2-flask-uwsgi-websocket 0.4.4-5
%obsolete python2-javaobj 0-0.9
%obsolete python2-krop 0.4.11-4
%obsolete python2-nikola 7.7.11-4
%obsolete python2-pyo 0.7.7-2
%obsolete python2-pyprintr 1.1-3
%obsolete python2-telegram-cli 1.3.3-0.6
%obsolete pytrailer 0.6.0-10
%obsolete ris-linux 0.4-18
%obsolete roundup 1.4.21-7
%obsolete rurple 1.0-0.14
%obsolete secstate 0.4.1-10
%obsolete spe 0.8.4.h-17
%obsolete system-config-network 1.6.11-8
%obsolete system-config-samba 1.2.100-6
%obsolete tmda 1.1.12-14
%obsolete trytond-ldap-connection 2.6.0-7
%obsolete twms 0.05-6

# Python 2 packages removed in Fedora 26 but never obsoleted
%obsolete PyKDE 3.16.7-10
%obsolete PyQt 3.18.1-36
%obsolete albumart 1.6.6-6
%obsolete ascend 0.9.10-12
%obsolete boom 0.8-5
%obsolete canl-c++-python 1.1.0-8
%obsolete dissy 10-7
%obsolete dnf-plugin-spacewalk 2.4.15-5
%obsolete flann-python 1.8.4-9
%obsolete fts-python 3.4.3-5
%obsolete glyphtracer 1.3-11
%obsolete iguanaIR-python 2:1.1.0-18
%obsolete kodos 2.4.9-20
%obsolete konkretcmpi-python 0.9.2-13
%obsolete kphotobymail 0.4.1-19
%obsolete ola-rdm-tests 0.10.3-2
%obsolete pipviewer 0.3.9-21
%obsolete pycmd 1.2-7
%obsolete pynetsnmp 0.28.14-15
%obsolete pynetsnmp-twisted 0.28.14-15
%obsolete python-SimpleCV 1.3-8
%obsolete python-akismet 0.2.0-10
%obsolete python-catwalk 2.0.2-13
%obsolete python-cement 2.2.2-8
%obsolete python-cherrytemplate 1.0.0-22
%obsolete python-compositor 0.2b-13
%obsolete python-condorec2e 1.3.1-8
%obsolete python-condorutils 1.5-13
%obsolete python-couchdbkit 0.6.5-7
%obsolete python-ctypesgen 0-0.8
%obsolete python-django-admin-honeypot 0.3.0-5
%obsolete python-django-authenticator 0.1.5-9
%obsolete python-django-bootstrap-toolkit 2.15.0-6
%obsolete python-django-dajax 0.9.2-7
%obsolete python-django-dajaxice 0.6-5
%obsolete python-django-dpaste 0.2.4-17
%obsolete python-django-pagination 1.0.7-10
%obsolete python-django-profile 0.6-0.9
%obsolete python-django-recaptcha-works 0.3.4-11
%obsolete python-django-roa 1.7-12
%obsolete python-django-sorting 0.1-13
%obsolete python-django-threaded-multihost 1.4.0-11
%obsolete python-django-tracking 0.3.7-16
%obsolete python-django-typepadapp 1.2.1-14
%obsolete python-dnf-plugins-extras-debug 0.0.12-5
%obsolete python-dnf-plugins-extras-leaves 0.0.12-5
%obsolete python-dnf-plugins-extras-local 0.0.12-5
%obsolete python-dnf-plugins-extras-repoclosure 0.0.12-5
%obsolete python-dnf-plugins-extras-repograph 0.0.12-5
%obsolete python-dnf-plugins-extras-repomanage 0.0.12-5
%obsolete python-dnf-plugins-extras-show-leaves 0.0.12-5
%obsolete python-dnf-plugins-extras-versionlock 0.0.12-5
%obsolete python-foolscap 0.10.1-3
%obsolete python-fpconst 0.7.3-18
%obsolete python-functest 0.8.8-10
%obsolete python-gudev 147.2-11
%obsolete python-import-utils 0.0.1-10
%obsolete python-kinterbasdb 3.3.0-14
%obsolete python-lirc 0.0.5-22
%obsolete python-logilab-common 0.63.2-7
%obsolete python-modargs 1.7-7
%obsolete python-multi-registry 0.0.2-10
%obsolete python-obexftp 0.24-14
%obsolete python-pebl 1.0.2-15
%obsolete python-prioritized-methods 0.2.1-16
%obsolete python-remoteobjects 1.2.1-4
%obsolete python-robofab 1.2.0-13
%obsolete python-ruledispatch 0.5a1-0.31
%obsolete python-snpp 1.1.2-13
%obsolete python-sphinx-theme-better 0.1.5-9
%obsolete python-tgcaptcha 0.11-19
%obsolete python-tgfastdata 0.9a7-0.10
%obsolete python-tpg 3.1.2-17
%obsolete python-turboflot 0.7.0-10
%obsolete python-tw-jquery 0.9.10-11
%obsolete python-typepad 2.0-9
%obsolete python-ufo2fdk 0.1-13
%obsolete python-webflash 0.1-0.15
%obsolete python-windmill 1.7-0.10
%obsolete python-wsgi-jsonrpc 0.2.9-9
%obsolete python-wsgiref 0.1.2-16
%obsolete python-xappy 0.6.0-0.10
%obsolete python-yumdaemon 0.9.2-12
%obsolete python2-RPi.GPIO 0.6.1-3
%obsolete python2-btrfs 5-2
%obsolete python2-freesteam 2.1-17
%obsolete python2-ola 0.10.3-2
%obsolete python2-pytg 0.4.10-4
%obsolete python2-tktable 2.10-14
%obsolete sfact 0.0-10
%obsolete skeinforge 12.03.14-21
%obsolete trac-condfieldsgenshi-plugin 0.2-5
%obsolete trac-defaultcc-plugin 0.3-0.8
%obsolete xchat-gnome 0.26.2-24
%obsolete zapplet 0.1-18

# Python 2 packages removed in Fedora 27 but never obsoleted
%obsolete VMDKstream 0.3-6
%obsolete conduit 0.3.17-15
%obsolete coot 0.8.8-3
%obsolete dtrx 7.1-11
%obsolete epylog 1.0.7-17
%obsolete fedfs-utils-python 0.10.5-5
%obsolete geany-plugins-geanypy 1.33-2
%obsolete grinder 0.0.139-10
%obsolete hotssh 0.2.7-13
%obsolete hotwire 0.721-18
%obsolete libcoot 0.8.8-3
%obsolete libpst-python 0.6.70-2
%obsolete magicor 1.1-19
%obsolete nautilus-phatch 0.2.7-28
%obsolete peppy 0.16.0-11
%obsolete pessulus 2.30.3-13
%obsolete phatch 0.2.7-28
%obsolete phatch-cli 0.2.7-28
%obsolete plague-client 0.4.5.8-34
%obsolete plague-common 0.4.5.8-34
%obsolete pymssql 1.0.2-7
%obsolete pyqtrailer 0.6.2-13
%obsolete python-OpenImageIO 1.7.15-2
%obsolete python-anfft 0.2-10
%obsolete python-appstream 0.8-3
%obsolete python-fedora-django 0.9.0-4
%obsolete python-forensic1394 0.2-17
%obsolete python-googlevoice 0.5-14
%obsolete python-numeric 24.2-28
%obsolete python-osbs 0.14-3
%obsolete python-zope-interface4 4.1.3-2
%obsolete python2-ProDy 1.8.2-9
%obsolete python2-coot 0.8.8-3
%obsolete python2-django-admin-honeypot 1.0.0-2
%obsolete python2-radicale 1.1.6-3
%obsolete reinteract 0.5.9-16
%obsolete relevation 1.3-5
%obsolete sslstrip 0.9-12
%obsolete supybot 0.83.4.1-18
%obsolete system-config-kdump 2.0.16-7
%obsolete v8-python 1:5.2.258-12
%obsolete xchat 1:2.8.8-35

# Python 2 packages removed in Fedora 28 but never obsoleted
%obsolete ansible-review 0.13.7-2
%obsolete cryptsetup-python 1.7.5-5
%obsolete fontmatrix 0.9.99-33
%obsolete ganglia-gmond-python 3.7.2-18
%obsolete gtk-recordmydesktop 0.3.8-20
%obsolete gtk-vnc-python 0.7.1-4
%obsolete libopensync-plugin-python 1:0.22-17
%obsolete libpst-python2 0.6.71-4
%obsolete mapserver-python 7.0.5-4
%obsolete marisa-python 0.2.4-25
%obsolete net-snmp-python 1:5.7.3-28
%obsolete openerp-client 6.1-13
%obsolete openerp7 7.0-12
%obsolete openscap-python 1.2.17-2
%obsolete openwsman-python 2.6.3-6
%obsolete preupgrade-assistant 2.1.9-5
%obsolete preupgrade-assistant-devel 2.1.9-5
%obsolete python-HTMLgen 2.2.2-27
%obsolete python-Lightbox 2.1-17
%obsolete python-NLopt 2.4.2-14
%obsolete python-PSI 0.3-0.17
%obsolete python-PyRSS2Gen 1.1-14
%obsolete python-TornadIO2 0.0.4-11
%obsolete python-UcsSdk 0.8.2.5-6
%obsolete python-ZSI 2.1-12
%obsolete python-amqpclt 0.6-2
%obsolete python-amqplib 1.0.2-18
%obsolete python-assertEquals 0.4.4-11
%obsolete python-astroML-addons 0.2.2-11
%obsolete python-babel-BabelGladeExtractor 0.2-0.14
%obsolete python-cryptominisat4 4.5.3-13
%obsolete python-di 0.3-10
%obsolete python-django-discover-runner 1.0-12
%obsolete python-django-kombu 0.9.4-10
%obsolete python-django-notification 1.2.0-9
%obsolete python-djvulibre 0.3.9-5
%obsolete python-gitapi 1.1.0-0.a3.6
%obsolete python-iptools 0.6.1-12
%obsolete python-kaa-base 0.6.0-18
%obsolete python-kaa-display 0.1.0-18
%obsolete python-kaa-imlib2 0.2.3-24
%obsolete python-kaa-metadata 0.7.7-17
%obsolete python-liblarch 2.1.0-11
%obsolete python-liblarch_gtk 2.1.0-11
%obsolete python-lmiwbem 0.7.2-16
%obsolete python-mecab 0.996-2
%obsolete python-mtTkinter 0.4-14
%obsolete python-mygpoclient 1.7-8
%obsolete python-narcissus-app 0.9.1-9
%obsolete python-narcissus-common 0.9.0.1-9
%obsolete python-narcissus-hub 0.9.0.1-9
%obsolete python-openhpi 1.2-0.18
%obsolete python-phacter 0.2.0-13
%obsolete python-repoze-what-pylons 1.0-18
%obsolete python-repoze-what-quickstart 1.0.9-13
%obsolete python-repoze-who-friendlyform 1.0.8-14
%obsolete python-repoze-who-testutil 1.0.1-13
%obsolete python-resultsdb_api 2.0.0-4
%obsolete python-rhev 1.0-16
%obsolete python-taskw 1.2.0-5
%obsolete python-txrequests 0.9.2-9
%obsolete python-urlobject 2.4.0-12
%obsolete python-xcffib 0.5.1-4
%obsolete python2-copr-common 0.2-2
%obsolete python2-django-cors-headers 2.0.2-4
%obsolete python2-django-helpdesk 0.2.10-2
%obsolete python2-django-jsonfield 1.0.3-6
%obsolete python2-django-keyedcache3 1.5.3-7
%obsolete python2-django-openstack-auth 2.4.2-3
%obsolete python2-django-picklefield 1.0.0-2
%obsolete python2-django-threadedcomments 1.2-3
%obsolete python2-django-tinymce 2.4.0-3
%obsolete python2-fedora-django 0.9.0-8
%obsolete python2-flufl-bounce 2.3-4
%obsolete python2-flufl-i18n 1.1.3-4
%obsolete python2-flufl-lock 2.4.1-4
%obsolete python2-lib389 1.0.4-3
%obsolete python2-libneurosim 0-3
%obsolete python2-libneurosim-mpich 0-3
%obsolete python2-libneurosim-openmpi 0-3
%obsolete python2-pydbus 0.6.0-4
%obsolete python2-pynlpl 1.1.2-4
%obsolete python2-rpy 2.8.6-9
%obsolete python2-trezor 0.7.16-4
%obsolete python2-udiskie 1.7.1-2
%obsolete qt-recordmydesktop 0.3.8-16
%obsolete rekall-python 2.4.6-39
%obsolete satyr-python 0.25-3
%obsolete scapy 2.3.3-3
%obsolete subscription-manager-gui 1.20.1-4
%obsolete wiredtiger-python 2.9.3-2

# Python 2 packages removed in Fedora 29 but never obsoleted
%obsolete StarCluster 1:0.95.6-11
%obsolete darkclient 0.2-12
%obsolete denyhosts 2.10-13
%obsolete firmware-addon-dell 2.2.9-13
%obsolete gnumed 1.6.7-7
%obsolete gtg 0.3.1-17
%obsolete gvrng 4.4-18
%obsolete libpagemap 0.0.1-25
%obsolete libsvm-python 3.21-4
%obsolete mlpack-python2 3.0.4-3
%obsolete pyrrd 0.1.0-9
%obsolete python-lettuce 0.2.20-3
%obsolete python-oslo-db-tests 4.17.0-3
%obsolete python-oslo-policy-tests 1.14.0-7
%obsolete python-oslo-reports-tests 1.17.0-4
%obsolete python-oslo-serialization-tests 2.20.0-3
%obsolete python2-abrt-doc 2.10.10-2
%obsolete python2-adapt 0.3.0-5
%obsolete python2-amqplib 1.0.2-20
%obsolete python2-ansible-inventory-grapher 2.4.5-3
%obsolete python2-ansible-review 0.13.7-4
%obsolete python2-ara 0.14.0-2
%obsolete python2-ara-tests 0.14.0-2
%obsolete python2-argcomplete 1.9.3-4
%obsolete python2-blivet 1:3.0.0-0.7
%obsolete python2-bytesize 1.4-2
%obsolete python2-cachecontrol 0.12.3-5
%obsolete python2-caja 1:1.20.2-3
%obsolete python2-ceilometerclient 2.6.1-6
%obsolete python2-clint 0.5.1-8
%obsolete python2-compose-utils 0.1.18-3
%obsolete python2-compyte 0.0.1-0.11
%obsolete python2-conu-pytest 0.7.1-3
%obsolete python2-coverage_pth 0.0.1-6
%obsolete python2-custodia-extra 0.5.0-12
%obsolete python2-djvulibre 0.8-3
%obsolete python2-docker-py 1:1.10.6-8
%obsolete python2-docx 0.8.5-13
%obsolete python2-dput 1.11-7
%obsolete python2-ee 3.0.0-3
%obsolete python2-fedmsg-atomic-composer 2017.1-4
%obsolete python2-flask-restless 0.17.0-8
%obsolete python2-fmn-sse 0.2.1-6
%obsolete python2-furl 1.0.1-3
%obsolete python2-gdl 0.9.9-7
%obsolete python2-geoip2 2.9.0-2
%obsolete python2-gevent-websocket 0.9.5-7
%obsolete python2-gradunwarp 1.0.3-7
%obsolete python2-gupnp-igd 0.2.5-3
%obsolete python2-i2c-tools 4.0-11
%obsolete python2-iksemel 1.5-0.2
%obsolete python2-ipa-desktop-profile-server 0.0.8-2
%obsolete python2-ipaserver 4.7.2-2
%obsolete python2-ipatests 4.7.2-2
%obsolete python2-iptools 0.6.1-15
%obsolete python2-ironic-inspector-client 1.9.0-6
%obsolete python2-libpfm 4.9.0-7
%obsolete python2-libpst 0.6.71-8
%obsolete python2-libstoragemgmt 1.7.3-2
%obsolete python2-libstoragemgmt-clibs 1.7.3-2
%obsolete python2-libvoikko 3.8-10
%obsolete python2-lmiwbem 0.7.2-19
%obsolete python2-ludolph 1.0.1-4
%obsolete python2-ludolph-zabbix 1.7-3
%obsolete python2-lvm-deprecated 2.02.177-6
%obsolete python2-mapserver 7.0.5-11
%obsolete python2-marisa 0.2.4-31
%obsolete python2-matplotlib-test-data 2.2.3-2
%obsolete python2-maxminddb 1.4.0-2
%obsolete python2-mlpy 3.5.0-8
%obsolete python2-mnemonic 0.17-4
%obsolete python2-mttkinter 0.4-17
%obsolete python2-narcissus-app 0.9.1-12
%obsolete python2-narcissus-common 0.9.0.1-12
%obsolete python2-narcissus-hub 0.9.0.1-11
%obsolete python2-net-snmp 1:5.7.3-39
%obsolete python2-networkmanager 2.0.1-5
%obsolete python2-nibabel 2.1.0-2
%obsolete python2-nipy 0.4.1-2
%obsolete python2-nose-cov 1.6-13
%obsolete python2-openhpi 1.2-0.21
%obsolete python2-openipmi 2.0.24-5
%obsolete python2-openstack-nose-plugin 0.11-15
%obsolete python2-orderedmultidict 0.7.11-6
%obsolete python2-parameterized 0.6.1-3
%obsolete python2-pbkdf2 1.3-9
%obsolete python2-phacter 0.2.0-15
%obsolete python2-pid 2.2.3-2
%obsolete python2-pki 10.6.9-2
%obsolete python2-pocketlint 0.17-2
%obsolete python2-prelude-correlator 4.0.0-3
%obsolete python2-prewikka 4.0.0-3
%obsolete python2-prov 1.5.1-4
%obsolete python2-pydicom 1.0.0-0.12
%obsolete python2-pygpgme 0.3-27
%obsolete python2-pynwb 0.6.1-4
%obsolete python2-pyopencl 2017.2.2-4
%obsolete python2-pysctp 0.6-13
%obsolete python2-pytest-multihost 3.0-2
%obsolete python2-pytest-sourceorder 0.5-10
%obsolete python2-pytest-testmon 0.9.6-4
%obsolete python2-pytools 2018.2-2
%obsolete python2-pywbem 0.12.6-2
%obsolete python2-ratelimitingfilter 0.6-2
%obsolete python2-repoze-what-pylons 1.0-20
%obsolete python2-requests-ftp 0.3.1-11
%obsolete python2-rnc2rng 2.5-3
%obsolete python2-rply 0.7.5-3
%obsolete python2-semver 2.7.8-3
%obsolete python2-serpy 0.2.0-3
%obsolete python2-sleekxmpp 1.3.2-4
%obsolete python2-sphinx-theme-flask git20130715.1cc4468-13
%obsolete python2-sqlacodegen 1.1.6-7
%obsolete python2-svgwrite 1.1.12-4
%obsolete python2-taskw 1.2.0-7
%obsolete python2-testfixtures 4.14.3-5
%obsolete python2-testfixtures-tests 4.14.3-5
%obsolete python2-tlslite 0.4.9-7
%obsolete python2-toro 1.0.1-6
%obsolete python2-transforms3d 0.3.1-3
%obsolete python2-trollius-redis 0.1.4-12
%obsolete python2-trololio 1.0-3
%obsolete python2-tweepy 3.5.0-7
%obsolete python2-txrequests 0.9.2-10
%obsolete python2-ufo2ft 1.1.0-4
%obsolete python2-urlobject 2.4.3-5
%obsolete python2-wiredtiger 3.0.0-2
%obsolete python2-workerpool 0.9.2-19
%obsolete python2-xcffib 0.5.1-6
%obsolete pywbem-twisted 0.12.6-2
%obsolete restauth 0.6.3-7
%obsolete supybot-git 0-10
%obsolete supybot-gribble 0.83.4.1-23
%obsolete supybot-irccat 0-11
%obsolete supybot-notify 0.2.2-14
%obsolete trac-ticketdelete-plugin 2.0-15
%obsolete trytond-calendar 4.0.1-5
%obsolete trytond-calendar-classification 4.0.1-5
%obsolete trytond-calendar-scheduling 4.0.1-5
%obsolete trytond-calendar-todo 4.0.1-5
%obsolete trytond-party-vcarddav 4.0.1-5
%obsolete wadofstuff-django-serializers 1.1.0-12
%obsolete xml2dict 0-0.14

# Python 2 packages removed in Fedora 30 but never obsoleted
%obsolete PyMunin 0.9.27-12
%obsolete Pyrex 0.9.9-19
%obsolete PythonCard 0.8.2-22
%obsolete ari-backup 1.0.12-10
%obsolete arm-none-eabi-gdb 7.6.2-5
%obsolete atomicapp 0.6.3-8
%obsolete aubio-python2 0.4.9-2
%obsolete bugyou 0.2.2-7
%obsolete bzr-fastimport 0.13.0-14
%obsolete bzrtools 2.6.0-11
%obsolete clusterPy 0.9.9-18
%obsolete cmdtest 0.32-2
%obsolete dnsyo 2.0.7-9
%obsolete feedstail 0.5.1-7
%obsolete gmpy 1.17-15
%obsolete gnome-hearts 0.3-24
%obsolete gnome-python2-gnomedesktop 2.32.0-34
%obsolete gnome-python2-libgtop2 2.32.0-34
%obsolete gnome-python2-totem 2.32.0-34
%obsolete gst-inspector 0.4-20
%obsolete hgsubversion 1.8.7-3
%obsolete ibus-py2override 1.5.19-19
%obsolete ibus-pygtk2 1.5.19-19
%obsolete lekhonee-lib 0.7-18
%obsolete lfc-python 1.10.0-11
%obsolete libkdtree++-python 0.7.0-9
%obsolete mMass 5.5.0-25
%obsolete mingw32-python2-pyqt5-sip 4.19.13-3
%obsolete mingw32-python2-sip 4.19.13-3
%obsolete mingw64-python2-pyqt5-sip 4.19.13-3
%obsolete mingw64-python2-sip 4.19.13-3
%obsolete ntop 5.0.1-16
%obsolete nwsserver 2.0.0-19
%obsolete obnam 1.21-8
%obsolete openerp 6.1-16
%obsolete os-apply-config 5.0.0-7
%obsolete os-collect-config 5.0.0-7
%obsolete os-net-config 5.0.0-7
%obsolete os-refresh-config 5.0.0-7
%obsolete ptpython2 0.41-9
%obsolete pyPdf 1.13-17
%obsolete pycanberra 0-0.19
%obsolete pygrace 0.4-20
%obsolete pyip 0.7-18
%obsolete pymunk 1.0.0-18
%obsolete pyrasite 2.0-10
%obsolete python-imgbased 1.0.999-0.2
%obsolete python-ironic-inspector-client 3.1.1-2
%obsolete python-manifestdestiny 0-0.16
%obsolete python-mozdevice 0-0.16
%obsolete python-mozhttpd 0-0.16
%obsolete python-mozinfo 0-0.16
%obsolete python-mozinstall 0-0.16
%obsolete python-mozlog 0-0.16
%obsolete python-mozprocess 0-0.16
%obsolete python-mozprofile 0-0.16
%obsolete python-mozrunner 0-0.16
%obsolete python-testing.postgresql 1.1.0-14
%obsolete python-webob1.1 1.1.1-18
%obsolete python-webtest1.3 1.3.4-17
%obsolete python2-4suite-xml 1.0.2-32
%obsolete python2-APLpy 1.1.1-8
%obsolete python2-APScheduler 3.5.3-2
%obsolete python2-CommonMark 0.7.5-4
%obsolete python2-ECPy 0.10.0-2
%obsolete python2-GeographicLib 1.49-6
%obsolete python2-GridDataFormats 0.5.0-2
%obsolete python2-ImcSdk 0.7.2-11
%obsolete python2-Mastodon 1.3.0-3
%obsolete python2-Naked 0.1.31-7
%obsolete python2-PyLEMS 0.4.9.1-2
%obsolete python2-PyLink 0.3.2-10
%obsolete python2-PyMySQL 0.9.2-3
%obsolete python2-Pympler 0.5-3
%obsolete python2-QtPy 1.4.2-4
%obsolete python2-SecretStorage 2.3.1-11
%obsolete python2-TGScheduler 1.7.0-12
%obsolete python2-Traits 4.6.0-2
%obsolete python2-TurboGears2 2.4.0a1-2
%obsolete python2-XStatic 1.0.1-15
%obsolete python2-XStatic-Angular-FileUpload 12.0.4.0-10
%obsolete python2-XStatic-jQuery 1.10.2.1-12
%obsolete python2-ZConfig 3.1.0-13
%obsolete python2-ZODB 5.4.0-5
%obsolete python2-aaargh 0.7.1-8
%obsolete python2-abclient 0.2.3-8
%obsolete python2-achoo 1.0-20
%obsolete python2-acme 0.39.0-2
%obsolete python2-adal 1.2.2-2
%obsolete python2-adduserpath 0.4.0-5
%obsolete python2-aexpect 1.5.1-4
%obsolete python2-affine 2.3.0-2
%obsolete python2-affinity 0.1.0-16
%obsolete python2-agate 1.6.1-4
%obsolete python2-agate-dbf 0.2.0-6
%obsolete python2-agate-excel 0.2.2-4
%obsolete python2-agate-sql 0.5.3-4
%obsolete python2-aiodns 1.1.1-5
%obsolete python2-alchimia 0.7.0-5
%obsolete python2-altgraph 0.12-17
%obsolete python2-amico 1.0.1-11
%obsolete python2-anfft 0.2-14
%obsolete python2-aniso8601 3.0.0-4
%obsolete python2-ansi 0.1.3-15
%obsolete python2-ansi2html 1.2.0-9
%obsolete python2-ansible-runner 1.0.5-2
%obsolete python2-ansible-tower-cli 3.3.0-5
%obsolete python2-ansicolor 0.2.4-9
%obsolete python2-ansicolors 1.1.8-7
%obsolete python2-anyconfig 0.9.7-2
%obsolete python2-anyjson 0.3.3-20
%obsolete python2-aodhclient 0.7.0-8
%obsolete python2-aodhclient-tests 0.7.0-8
%obsolete python2-apptools 4.4.0-13
%obsolete python2-argparse-manpage 1.2.2-2
%obsolete python2-args 0.1.0-9
%obsolete python2-asciitable 0.8.0-23
%obsolete python2-asciitree 0.3.3-10
%obsolete python2-assertequals 0.4.4-15
%obsolete python2-astral 1.6.1-4
%obsolete python2-astroML 0.3-22
%obsolete python2-astroid 1.6.4-3
%obsolete python2-astroml-addons 0.2.2-18
%obsolete python2-astropy-helpers 2.0.4-5
%obsolete python2-astroquery 0.3.8-3
%obsolete python2-asttokens 1.1.10-4
%obsolete python2-atfork 0.1.2-17
%obsolete python2-atomic-reactor 1.6.36.1-4
%obsolete python2-atomic-reactor-koji 1.6.36.1-4
%obsolete python2-atomic-reactor-metadata 1.6.36.1-4
%obsolete python2-atomic-reactor-rebuilds 1.6.36.1-4
%obsolete python2-atpy 0.9.7-18
%obsolete python2-auth-credential 1.0-18
%obsolete python2-automaton 1.14.0-4
%obsolete python2-autopep8 1.2.4-10
%obsolete python2-avocado 52.1-8
%obsolete python2-avocado-plugins-output-html 52.1-8
%obsolete python2-avocado-plugins-resultsdb 52.1-8
%obsolete python2-avocado-plugins-runner-docker 52.1-8
%obsolete python2-avocado-plugins-runner-remote 52.1-8
%obsolete python2-avocado-plugins-runner-vm 52.1-8
%obsolete python2-avocado-plugins-varianter-yaml-to-mux 52.1-8
%obsolete python2-azure-devtools 1.0.0-5
%obsolete python2-azure-sdk 4.0.0-6
%obsolete python2-azure-storage 1.4.0-2
%obsolete python2-babel-babelgladeextractor 0.2-0.17
%obsolete python2-babelfish 0.5.5-12
%obsolete python2-backlash 0.1.4-2
%obsolete python2-backports-csv 1.0.5-6
%obsolete python2-backports-shutil_get_terminal_size 1.0.0-8
%obsolete python2-backports-shutil_which 3.5.1-8
%obsolete python2-baker 1.3-10
%obsolete python2-bash8 0.1.1-17
%obsolete python2-bashate 0.5.1-10
%obsolete python2-batchhttp 1.1.1-14
%obsolete python2-batinfo 0.4.2-10
%obsolete python2-beaker 1.10.0-2
%obsolete python2-beanstalkc 0.4.0-10
%obsolete python2-bigsuds 1.0.6-5
%obsolete python2-binaryornot 0.4.3-3
%obsolete python2-binstruct 1.0.1-8
%obsolete python2-bintrees 2.0.1-17
%obsolete python2-biopython 1.72-3
%obsolete python2-bitarray 0.8.3-4
%obsolete python2-bitmath 1.3.1-2
%obsolete python2-bitstring 3.1.6-2
%obsolete python2-bitstruct 3.7.0-5
%obsolete python2-blessed 1.15.0-5
%obsolete python2-blivet1 1:1.20.4-5
%obsolete python2-bloom 0.9.0-2
%obsolete python2-bodhi 3.12.0-201
%obsolete python2-bodhi-client 3.12.0-201
%obsolete python2-booleanoperations 0.8.0-4
%obsolete python2-botocore 1.10.41-5
%obsolete python2-bottle-sqlite 0.1.3-8
%obsolete python2-brian2 2.2-2
%obsolete python2-brotli 1.0.5-2
%obsolete python2-bson 3.7.2-2
%obsolete python2-btchip 0.1.28-2
%obsolete python2-bucky 2.3.0-4
%obsolete python2-bugzilla2fedmsg 0.3.1-2
%obsolete python2-bz2file 0.98-8
%obsolete python2-caca 0.99-0.37
%obsolete python2-cachetools 2.1.0-4
%obsolete python2-cachez 0.1.2-7
%obsolete python2-cagraph 1.2-25
%obsolete python2-cairocffi 0.7.2-14
%obsolete python2-camel 0.1.2-6
%obsolete python2-canonicaljson 1.1.3-4
%obsolete python2-cantor 18.04.3-3
%obsolete python2-carbon 1.1.4-2
%obsolete python2-carrot 0.10.7-18
%obsolete python2-cartopy 0.17.0-3
%obsolete python2-castellan 0.5.0-6
%obsolete python2-catkin_lint 1.6.2-2
%obsolete python2-catkin_tools 0.4.5-2
%obsolete python2-cattrs 0.9.0-2
%obsolete python2-ccdproc 1.3.0-4
%obsolete python2-cclib 1.3.2-11
%obsolete python2-ceilometermiddleware 0.5.0-7
%obsolete python2-cerberus 1.2-2
%obsolete python2-cerealizer 0.8-10
%obsolete python2-certbot 0.39.0-2
%obsolete python2-certbot-apache 0.39.0-2
%obsolete python2-certbot-dns-cloudflare 0.39.0-2
%obsolete python2-certbot-dns-cloudxns 0.39.0-2
%obsolete python2-certbot-dns-digitalocean 0.39.0-2
%obsolete python2-certbot-dns-dnsimple 0.39.0-2
%obsolete python2-certbot-dns-dnsmadeeasy 0.39.0-2
%obsolete python2-certbot-dns-gehirn 0.39.0-2
%obsolete python2-certbot-dns-google 0.39.0-2
%obsolete python2-certbot-dns-linode 0.39.0-2
%obsolete python2-certbot-dns-luadns 0.39.0-2
%obsolete python2-certbot-dns-nsone 0.39.0-2
%obsolete python2-certbot-dns-ovh 0.39.0-2
%obsolete python2-certbot-dns-rfc2136 0.39.0-2
%obsolete python2-certbot-dns-route53 0.39.0-2
%obsolete python2-certbot-dns-sakuracloud 0.39.0-2
%obsolete python2-certbot-nginx 0.39.0-2
%obsolete python2-chaospy 3.0.7-2
%obsolete python2-characteristic 14.3.0-14
%obsolete python2-cherrypy2 2.3.0-31
%obsolete python2-citeproc-py 0.4.0-5
%obsolete python2-cjson 1.2.1-7
%obsolete python2-clang 7.0.1-7
%obsolete python2-cli 1.2-16
%obsolete python2-click-completion 0.3.1-2
%obsolete python2-click-log 0.3.2-4
%obsolete python2-click-man 0.2.2-5
%obsolete python2-click-plugins 1.1.1-2
%obsolete python2-click-threading 0.4.4-6
%obsolete python2-clientform 0.2.10-17
%obsolete python2-cliff-tablib 1.1-15
%obsolete python2-cliff-tests 2.13.0-3
%obsolete python2-cligj 0.4.0-7
%obsolete python2-cloud-sptheme 1.7.1-9
%obsolete python2-cloudflare 2.3.0-2
%obsolete python2-cloudpickle 0.3.1-5
%obsolete python2-clyent 1.2.2-8
%obsolete python2-cma 1.1.7-8
%obsolete python2-cmd2 0.8.8-6
%obsolete python2-cmigemo 0.1.6-12
%obsolete python2-colander 1.4-6
%obsolete python2-collectd-ceilometer-plugin 1.0.1-8
%obsolete python2-colorama 0.4.0-4
%obsolete python2-colorlog 3.1.4-4
%obsolete python2-colorspacious 1.1.2-4
%obsolete python2-colour-runner 0.0.4-14
%obsolete python2-columnize 0.3.9-9
%obsolete python2-concurrentloghandler 0.9.1-9
%obsolete python2-conda 4.5.13-2
%obsolete python2-configargparse 0.14.0-3
%obsolete python2-configshell 1:1.1.fb25-3
%obsolete python2-confparser 1.0.1-21
%obsolete python2-congressclient 1.5.0-8
%obsolete python2-congressclient-tests 1.5.0-8
%obsolete python2-contexttimer 0.3.1-12
%obsolete python2-conu 0.4.0-4
%obsolete python2-cookiecutter 1.6.0-6
%obsolete python2-cookies 2.2.1-14
%obsolete python2-cornice 3.1.0-4
%obsolete python2-cornice-sphinx 1:0.3-7
%obsolete python2-couchbase 2.5.4-2
%obsolete python2-couchdb 1.0-12
%obsolete python2-cov-core 1.15.0-12
%obsolete python2-cpio 0.1-31
%obsolete python2-cpuinfo 4.0.0-4
%obsolete python2-cram 0.6-18
%obsolete python2-crane 3.1.1-3
%obsolete python2-crank 0.8.1-7
%obsolete python2-createrepo_c 0.14.2-2
%obsolete python2-croniter 0.3.19-5
%obsolete python2-csdiff 1.6.1-2
%obsolete python2-cssmin 0.2.0-14
%obsolete python2-ctrldaemon 0.2-12
%obsolete python2-cu2qu 1.5.0-5
%obsolete python2-cursive 0.1.2-7
%obsolete python2-custodia 0.6.0-5
%obsolete python2-cvss 1.10-2
%obsolete python2-cytoolz 0.9.0.1-6
%obsolete python2-daemonize 2.4.7-7
%obsolete python2-daiquiri 1.2.1-5
%obsolete python2-datanommer-consumer 0.8.1-5
%obsolete python2-dateutil15 1.5-16
%obsolete python2-dbf 0.96.005-11
%obsolete python2-dbfread 2.0.7-8
%obsolete python2-ddt 1.2.1-2
%obsolete python2-deap 1.0.1-10
%obsolete python2-debconf 1.5.69-2
%obsolete python2-debian 0.1.32-4
%obsolete python2-debrepo 0.0.3-10
%obsolete python2-debtcollector 1.11.0-7
%obsolete python2-decoratortools 1.8-18
%obsolete python2-deepdiff 3.3.0-4
%obsolete python2-defcon 0.5.1-4
%obsolete python2-deltasigma 0.2-15
%obsolete python2-descartes 1.1.0-9
%obsolete python2-dialog 3.3.0-16
%obsolete python2-dict-sorted 1.0.0-9
%obsolete python2-diff-cover 0.9.12-5
%obsolete python2-diff-match-patch 20121119-6
%obsolete python2-digitalocean 1.14.0-2
%obsolete python2-dill 0.2.7.1-6
%obsolete python2-dingus 0.3.4-16
%obsolete python2-distlib 0.2.7-2
%obsolete python2-distro 1.3.0-5
%obsolete python2-distro-info 0.18-2
%obsolete python2-distroinfo 0.3.0-2
%obsolete python2-django-tagging 0.4.6-5
%obsolete python2-dlrn 0.5.1-6
%obsolete python2-dns-lexicon 3.3.4-3
%obsolete python2-docker-pycreds 0.3.0-4
%obsolete python2-docker-squash 1.0.7-4
%obsolete python2-dockerpty 0.4.1-13
%obsolete python2-dogtail 0.9.11-2
%obsolete python2-dominate 2.3.1-6
%obsolete python2-dopy 0.3.7-10
%obsolete python2-drat 0.4.2-15
%obsolete python2-duecredit 0.7.0-2
%obsolete python2-dumptruck 0.1.6-12
%obsolete python2-durus 3.9-20
%obsolete python2-easyargs 0.9.4-6
%obsolete python2-ecdsa 0.13.3-2
%obsolete python2-ecryptfs-utils 111-16
%obsolete python2-editorconfig 0.12.0-12
%obsolete python2-efel 3.0.58-2
%obsolete python2-elasticsearch 2.4.0-9
%obsolete python2-email_reply_parser 0.3.0-20140523git76e9481.14
%obsolete python2-emcee 2.2.1-10
%obsolete python2-enlighten 1.3.0-2
%obsolete python2-entrypoints 0.2.3-10
%obsolete python2-enzyme 0.4.1-6
%obsolete python2-epi 0.1-12
%obsolete python2-epub 0.5.2-15
%obsolete python2-et_xmlfile 1.0.1-13
%obsolete python2-etcd 0.4.5-13
%obsolete python2-etcd3gw 0.2.4-8
%obsolete python2-evdev 1.1.2-2
%obsolete python2-events 0.3-3
%obsolete python2-evic 0.1-0.13
%obsolete python2-exabgp 4.0.5-8
%obsolete python2-f5-icontrol-rest 1.3.9-5
%obsolete python2-f5-sdk 3.0.18-2
%obsolete python2-fabric 2.0.0-5
%obsolete python2-fadvise 5.0.0-9
%obsolete python2-faker 0.9.0-2
%obsolete python2-fastavro 0.19.8-4
%obsolete python2-fastimport 0.9.8-4
%obsolete python2-faulthandler 3.1-3
%obsolete python2-fauxquests 1.1-8
%obsolete python2-fdb 1.8-5
%obsolete python2-fedimg 2.3.0-3
%obsolete python2-fedmsg-genacls 0.6-7
%obsolete python2-fedmsg-rabbitmq-serializer 0.0.5-9
%obsolete python2-feedcache 1.4.1-11
%obsolete python2-feedgen 0.7.0-4
%obsolete python2-feedgenerator 1.9-7
%obsolete python2-ferari 0.2.0-20
%obsolete python2-fiat 1.6.0-13
%obsolete python2-filelock 2.0.8-8
%obsolete python2-filetype 1.0.0-6
%obsolete python2-fiona 1.8.6-2
%obsolete python2-firehose 0.5-7
%obsolete python2-firkin 0.02-21
%obsolete python2-fitsio 0.9.11-9
%obsolete python2-flake8-import-order 0.18-3
%obsolete python2-flask-admin 1.5.2-2
%obsolete python2-flask-assets 0.10-14
%obsolete python2-flask-autoindex 0.6-4
%obsolete python2-flask-babelex 0.9.3-4
%obsolete python2-flask-bootstrap 3.3.7.1-6
%obsolete python2-flask-cache 0.13.1-14
%obsolete python2-flask-classy 0.6.10-9
%obsolete python2-flask-debugtoolbar 0.10.0-11
%obsolete python2-flask-gravatar 0.5.0-4
%obsolete python2-flask-htmlmin 1.4.0-3
%obsolete python2-flask-httpauth 3.2.3-8
%obsolete python2-flask-images 2.1.2-10
%obsolete python2-flask-lastuser 0.2-16
%obsolete python2-flask-login 0.4.1-4
%obsolete python2-flask-mail 0.9.1-5
%obsolete python2-flask-mako 0.4-10
%obsolete python2-flask-multistatic 1.0-10
%obsolete python2-flask-oauth 0.13-9
%obsolete python2-flask-oidc 1.4.0-2
%obsolete python2-flask-paranoid 0.2.0-5
%obsolete python2-flask-principal 0.4.0-18
%obsolete python2-flask-restful 0.3.6-9
%obsolete python2-flask-rstpages 0.3-16
%obsolete python2-flask-security 3.0.0-4
%obsolete python2-flask-silk 0.2-4
%obsolete python2-flask-sphinx-themes 1.0.2-4
%obsolete python2-flask-whooshalchemy 0.6-16
%obsolete python2-flask-whooshee 0.4.1-9
%obsolete python2-flask-xml-rpc 0.1.2-14
%obsolete python2-flatland 0.0.2-17
%obsolete python2-flatpak-module-tools 0.11.1-2
%obsolete python2-flock 0.1-15
%obsolete python2-fmf 0.6-2
%obsolete python2-fmn-rules 0.9.1-8
%obsolete python2-fmn-web 0.8.1-9
%obsolete python2-fn 0.4.3-13
%obsolete python2-fontMath 0.4.4-5
%obsolete python2-fontdump 1.3.0-13
%obsolete python2-fontname 0.2.0-14
%obsolete python2-formats 0.1.1-12
%obsolete python2-freetype 2.0-2
%obsolete python2-frozen-flask 0.12-11
%obsolete python2-frozendict 1.2-8
%obsolete python2-fsmonitor 0.1-15
%obsolete python2-fts 3.8.3-2
%obsolete python2-fuckit 4.8.0-16
%obsolete python2-funcparserlib 0.3.6-18
%obsolete python2-functools32 3.2.3.2-7
%obsolete python2-futurist 1.7.0-2
%obsolete python2-fuzzyfinder 2.1.0-3
%obsolete python2-fuzzywuzzy 0.7.0-11
%obsolete python2-gabbi 1.42.1-5
%obsolete python2-gasp 0.3.2-17
%obsolete python2-gatspy 0.3-11
%obsolete python2-gccinvocation 0.1-18
%obsolete python2-gear 0.11.0-6
%obsolete python2-gearbox 0.1.1-13
%obsolete python2-gensim-core 0.10.0-16
%obsolete python2-geojson 1.3.0-13
%obsolete python2-geopandas 0.5.0-2
%obsolete python2-gerrit 0.0.1-15
%obsolete python2-gerrymander 1.5-13
%obsolete python2-gevent-socketio 0.3.6-10
%obsolete python2-gfm 0.1.3-10
%obsolete python2-giacpy 0.6.8-2
%obsolete python2-ginga 2.6.5-6
%obsolete python2-gitapi 1.1.0-0.a3.11
%obsolete python2-github3py 1.0.0-0.9
%obsolete python2-gitlab 1.3.0-6
%obsolete python2-glance-store 0.9.1-9
%obsolete python2-glances 2.11.1-6
%obsolete python2-glob2 0.6.0-6
%obsolete python2-gluster 4.1.5-2
%obsolete python2-glyphsLib 2.2.1-5
%obsolete python2-gnocchiclient 7.0.4-2
%obsolete python2-gnocchiclient-tests 7.0.4-2
%obsolete python2-gofer 2.12.1-4
%obsolete python2-gofer-amqp 2.12.1-4
%obsolete python2-gofer-proton 2.12.1-4
%obsolete python2-gofer-qpid 2.12.1-4
%obsolete python2-google-auth 1:1.1.1-2
%obsolete python2-googletrans 2.2.0-6
%obsolete python2-gr-iio 0.2-8
%obsolete python2-grabbit 0.2.6-2
%obsolete python2-grafyaml 0.0.5-10
%obsolete python2-graphitesend 0.10.0-8
%obsolete python2-gsd 1.7.0-2
%obsolete python2-gtts 2.0.1-5
%obsolete python2-gtts-token 1.1.1-10
%obsolete python2-guessit 2.1.4-9
%obsolete python2-gzipstream 2.8.6-4
%obsolete python2-h5io 0.1.0-3
%obsolete python2-halite 0.1.16-13
%obsolete python2-hdfs 2.5.8-2
%obsolete python2-heapdict 1.0.0-7
%obsolete python2-heketi 8.0.0-2
%obsolete python2-hexdump 3.4-0.6
%obsolete python2-hgapi 1.7.4-6
%obsolete python2-hghooks 0.7.0-11
%obsolete python2-hivex 1.3.17-2
%obsolete python2-honcho 1.0.1-2
%obsolete python2-htmlgen 2.2.2-33
%obsolete python2-htmlmin 0.1.12-6
%obsolete python2-httmock 1.2.6-4
%obsolete python2-http-client 3.1.0-4
%obsolete python2-httpwatcher 0.5.1-4
%obsolete python2-humanize 0.5.1-15
%obsolete python2-husl 4.0.3-11
%obsolete python2-hwdata 2.3.7-4
%obsolete python2-i3ipc 1.5.1-2
%obsolete python2-idstools 0.6.3-6
%obsolete python2-importanize 0.6.3-6
%obsolete python2-importmagic 0.1.7-10
%obsolete python2-indexed_gzip 0.8.10-2
%obsolete python2-inflect 0.3.1-2
%obsolete python2-influxdb 5.2.0-2
%obsolete python2-inifile 0.3-12
%obsolete python2-inlinestyler 0.1.7-12
%obsolete python2-inotify_simple 1.1.8-2
%obsolete python2-instant 2016.1.0-8
%obsolete python2-interfile 0.3.1-10
%obsolete python2-invocations 0.13.0-10
%obsolete python2-iowait 0.2-8
%obsolete python2-ipa-desktop-profile-client 0.0.8-5
%obsolete python2-ipdb 0.12.2-2
%obsolete python2-ipgetter 0.6-13
%obsolete python2-iptables 0.12.0-5
%obsolete python2-irawadi-user 0.1-17
%obsolete python2-irclib 0.4.8-17
%obsolete python2-iso-639 0.4.5-6
%obsolete python2-iso3166 1.0-2
%obsolete python2-iso639 0.1.4-7
%obsolete python2-isomd5sum 1:1.2.3-4
%obsolete python2-ivi 0.14.9-14
%obsolete python2-j1m.sphinxautointerface 0.3.0-7
%obsolete python2-j1m.sphinxautozconfig 0.1.0-4
%obsolete python2-jabberpy 0.5-0.42
%obsolete python2-jaydebeapi 1.1.1-6
%obsolete python2-jcconv 0.2.4-9
%obsolete python2-jdcal 1.4-2
%obsolete python2-jellyfish 0.6.0-4
%obsolete python2-jinja2-cli 0.6.0-7
%obsolete python2-jinja2-time 0.2.0-5
%obsolete python2-jinja2_pluralize 0.3.0-13
%obsolete python2-jira 2.0.0-2
%obsolete python2-joblib 0.11-7
%obsolete python2-josepy 1.2.0-2
%obsolete python2-jsmin 2.2.2-5
%obsolete python2-json-logger 0.1.7-6
%obsolete python2-jsonmodels 2.2-6
%obsolete python2-jsonpatch 1.21-5
%obsolete python2-jsonrpclib 0.3.1-5
%obsolete python2-junit_xml 1.8-5
%obsolete python2-justbases 0.9-8
%obsolete python2-justbytes 0.11-5
%obsolete python2-k8sclient 0.3.0-9
%obsolete python2-kafka 1.4.3-2
%obsolete python2-kaptan 0.5.5-7
%obsolete python2-kdcproxy 0.4-3
%obsolete python2-keyczar 0.71c-13
%obsolete python2-keyring 13.2.1-4
%obsolete python2-keystoneclient-kerberos 0.3.0-9
%obsolete python2-keystonemiddleware 4.21.0-2
%obsolete python2-kgb 0.5.1-11
%obsolete python2-kid 0.9.6-23
%obsolete python2-klusta 3.0.16-7
%obsolete python2-kobo-admin 0.8.0-2
%obsolete python2-kobo-django 0.8.0-2
%obsolete python2-kobo-hub 0.8.0-2
%obsolete python2-krbcontext 0.8-7
%obsolete python2-kubernetes 10.0.1-2
%obsolete python2-kubernetes-tests 10.0.1-2
%obsolete python2-lasagne 0.1-11
%obsolete python2-lazr-config 2.1-8
%obsolete python2-lazr-delegates 2.0.3-8
%obsolete python2-lazy-object-proxy 1.3.1-8
%obsolete python2-lazyarray 0.3.2-2
%obsolete python2-ldaphelper 1.0.1-21
%obsolete python2-ldappool 2.1.0-4
%obsolete python2-ldaptor 16.0.1-4
%obsolete python2-leather 0.3.3-8
%obsolete python2-lesscpy 0.13.0-7
%obsolete python2-libNeuroML 0.2.47-2
%obsolete python2-libcnml 0.9.5-10
%obsolete python2-libnacl 1.6.1-5
%obsolete python2-libpamtest 1.0.7-2
%obsolete python2-libqutrub 1.0-13
%obsolete python2-librosa 0.5.1-7
%obsolete python2-libsss_nss_idmap 2.2.2-4
%obsolete python2-libtmux 0.6.0-6
%obsolete python2-libusb1 1.6.4-4
%obsolete python2-lightblue 0.1.4-4
%obsolete python2-lightbox 2.1-20
%obsolete python2-linux-procfs 0.6.1-2
%obsolete python2-listquote 1.4.0-16
%obsolete python2-livereload 2.5.2-3
%obsolete python2-locket 0.2.0-10
%obsolete python2-logbook 1.0.0-13
%obsolete python2-logging-tree 1.7-10
%obsolete python2-logutils 0.3.5-7
%obsolete python2-logzero 1.3.1-6
%obsolete python2-ly 0.9.5-9
%obsolete python2-lyricwiki 0.1.35-19
%obsolete python2-magnumclient-tests 2.9.1-2
%obsolete python2-maps 4.2.0-6
%obsolete python2-marathon 0.8.8-8
%obsolete python2-markups 2.0.0-11
%obsolete python2-marrow-mailer 4.0.2-10
%obsolete python2-marrow-util 1.2.3-9
%obsolete python2-marshmallow 2.11.1-9
%obsolete python2-marshmallow-enum 1.4.1-5
%obsolete python2-martian 0.15-5
%obsolete python2-matrix-synapse-ldap3 0.1.3-2
%obsolete python2-mccabe 0.6.1-10
%obsolete python2-mdp 3.5-13
%obsolete python2-meld3 1.0.2-9
%obsolete python2-meliae 0.4.0-19
%obsolete python2-messaging 1.1-13
%obsolete python2-metar 1.5.0-7
%obsolete python2-microversion-parse 0.1.3-10
%obsolete python2-mimerender 0.5.5-11
%obsolete python2-ming 0.4.9-0.3
%obsolete python2-minimock 1.2.8-18
%obsolete python2-mitogen 0.2.8-2
%obsolete python2-mmtf 1.1.2-4
%obsolete python2-mne 0.13.1-9
%obsolete python2-mne-bids 0.2-2
%obsolete python2-molecule 2.19-3
%obsolete python2-mongoengine 0.15.3-2
%obsolete python2-mongoquery 1.3.3-3
%obsolete python2-moss 0.5.0-4
%obsolete python2-mpd 0.2.1-20
%obsolete python2-msrest 0.6.10-2
%obsolete python2-msrestazure 0.6.2-2
%obsolete python2-mtg 1.6.1-8
%obsolete python2-munkres 1.0.12-8
%obsolete python2-murano-pkg-check 0.3.0-10
%obsolete python2-mutatormath 2.1.0-5
%obsolete python2-mwlib-docbook 0.1.0-17
%obsolete python2-mwlib-xhtml 0.1.0-17
%obsolete python2-myghty 1.2-16
%obsolete python2-mygpoclient 1.8-5
%obsolete python2-myhdl 0.10-2
%obsolete python2-naftawayh 0.2-14
%obsolete python2-natsort 5.3.3-2
%obsolete python2-nb2plots 0.6-3
%obsolete python2-nbxmpp 0.6.10-2
%obsolete python2-ncclient 0.4.7-9
%obsolete python2-nectar 1.5.6-5
%obsolete python2-neo 0.8.0-0.2
%obsolete python2-neovim 0.3.2-1
%obsolete python2-netdiff 0.4.7-11
%obsolete python2-netjsonconfig 0.5.3-7
%obsolete python2-netlib 0.15-10
%obsolete python2-netmiko 2.2.2-2
%obsolete python2-networking-bigswitch 2015.3.12-6
%obsolete python2-neutronclient-tests 6.7.0-2
%obsolete python2-newt_syrup 0.2.0-15
%obsolete python2-nineml 1.0.1-3
%obsolete python2-nixio 1.4.6-2
%obsolete python2-nmap 0.6.1-10
%obsolete python2-nmrglue 0.7-2
%obsolete python2-nodeenv 0.13.6-14
%obsolete python2-nose-parameterized 0.3.5-14
%obsolete python2-nose2 0.7.4-3
%obsolete python2-nose_warnings_filters 0.1.5-7
%obsolete python2-notario 0.0.14-4
%obsolete python2-notmuch 0.27-5
%obsolete python2-novaclient-os-networks 0.26-9
%obsolete python2-novaclient-os-virtual-interfaces 0.20-9
%obsolete python2-nsdf 0.0-10
%obsolete python2-ntplib 0.3.3-13
%obsolete python2-num2words 0.5.7-3
%obsolete python2-numdisplay 1.5.6-21
%obsolete python2-octaviaclient 1.3.0-7
%obsolete python2-octaviaclient-tests 1.3.0-7
%obsolete python2-odict 1.5.1-12
%obsolete python2-offtrac 0.1.0-16
%obsolete python2-ofxparse 0.18-3
%obsolete python2-okaara 1.0.37-7
%obsolete python2-openimageio 1.8.16-2
%obsolete python2-openoffice 0.1-0.29
%obsolete python2-openopt 0.5625-11
%obsolete python2-openpyxl 2.5.4-4
%obsolete python2-optcomplete 1.2-0.20
%obsolete python2-os-brick 1.6.1-8
%obsolete python2-os-service-types 1.1.0-7
%obsolete python2-os-win 2.2.0-7
%obsolete python2-osbs-client 0.52-3
%obsolete python2-oslo-cache-tests 1.28.0-2
%obsolete python2-oslo-middleware 3.34.0-2
%obsolete python2-oslo-middleware-tests 3.34.0-2
%obsolete python2-oslo-policy-tests 1.33.2-2
%obsolete python2-oslo-privsep-tests 1.13.0-8
%obsolete python2-oslo-reports 1.26.0-2
%obsolete python2-oslo-reports-tests 1.26.0-2
%obsolete python2-oslo-rootwrap 5.13.0-2
%obsolete python2-oslo-rootwrap-tests 5.13.0-2
%obsolete python2-oslo-serialization-tests 2.24.0-2
%obsolete python2-oslo-sphinx 4.18.0-2
%obsolete python2-oslo-versionedobjects-tests 1.31.3-2
%obsolete python2-oslo-vmware-tests 2.26.0-2
%obsolete python2-oslotest 3.2.0-2
%obsolete python2-osprofiler 1.11.0-6
%obsolete python2-osrf-pycommon 0.1.9-2
%obsolete python2-pacpy 1.0.3.1-3
%obsolete python2-paho-mqtt 1.3.1-5
%obsolete python2-paida 3.2.1_2.10.1-19
%obsolete python2-pamela 0.3.0-7
%obsolete python2-pandocfilters 1.4.1-6
%obsolete python2-pankoclient 0.3.0-6
%obsolete python2-pankoclient-tests 0.3.0-6
%obsolete python2-parallel-ssh 0.91.2-9
%obsolete python2-parse 1.8.4-2
%obsolete python2-parse_type 0.4.2-2
%obsolete python2-parsel 1.5.0-3
%obsolete python2-partd 1.0.0-2
%obsolete python2-pathspec 0.5.3-7
%obsolete python2-patool 1.12-5
%obsolete python2-patsy 0.5.0-4
%obsolete python2-pcp 5.0.1-2
%obsolete python2-pdfkit 0.5.0-12
%obsolete python2-pdfminer 20181108-2
%obsolete python2-pdir2 0.3.0-5
%obsolete python2-peak-rules 0.5a1.dev-30
%obsolete python2-peak-util-addons 0.7-19
%obsolete python2-peak-util-assembler 0.6-17
%obsolete python2-peak-util-extremes 1.1.1-18
%obsolete python2-peak-util-symbols 1.0-22
%obsolete python2-pecan 1.3.2-5
%obsolete python2-pecan-notario 0.0.3-13
%obsolete python2-peewee 2.10.2-8
%obsolete python2-pefile 2017.11.5-5
%obsolete python2-perf 5.3.11-101
%obsolete python2-persist-queue 0.4.0-4
%obsolete python2-petlink 0.3.4-2
%obsolete python2-pg8000 1.12.2-3
%obsolete python2-pgpdump 1.5-12
%obsolete python2-pgu 0.12.3-21
%obsolete python2-phabricator 0.7.0-7
%obsolete python2-phonenumbers 8.9.0-4
%obsolete python2-photutils 0.4-8
%obsolete python2-phyghtmap 2.20-2
%obsolete python2-pickleshare 0.7.4-11
%obsolete python2-piexif 1.0.13-5
%obsolete python2-pifpaf 1.1.0-7
%obsolete python2-pika-pool 0.1.3-13
%obsolete python2-pkgwat-api 0.12-18
%obsolete python2-plaintable 0.1.1-12
%obsolete python2-pluginbase 0.7-4
%obsolete python2-pluginlib 0.6.1-2
%obsolete python2-podcastparser 0.6.3-6
%obsolete python2-port-for 0.4-7
%obsolete python2-portalocker 1.2.1-3
%obsolete python2-positional 1.1.1-10
%obsolete python2-pottymouth 2.2.1-15
%obsolete python2-power 1.4-14
%obsolete python2-poyo 0.4.1-4
%obsolete python2-pretty 0.1-18
%obsolete python2-proboscis 1.2.6.0-13
%obsolete python2-profilehooks 1.9.0-9
%obsolete python2-progress 1.4-3
%obsolete python2-proliantutils 2.2.0-6
%obsolete python2-prometheus_client 0.6.0-2
%obsolete python2-prompt_toolkit 1.0.16-2
%obsolete python2-psycogreen 1.0-8
%obsolete python2-publicsuffix 1.1.0-7
%obsolete python2-py-radix 0.9.3-12
%obsolete python2-py2neo 3.1.2-10
%obsolete python2-py2pack 0.6.3-10
%obsolete python2-py9p 1.0.9-15
%obsolete python2-pyModbusTCP 0.1.5-7
%obsolete python2-pyactivetwo 0.1-10
%obsolete python2-pyaes 1.6.0-6
%obsolete python2-pyarabic 0.4-13
%obsolete python2-pybeam 0.3.2-13
%obsolete python2-pyblock 0.53-19
%obsolete python2-pybtex-docutils 0.2.1-11
%obsolete python2-pycallgraph 0.5.1-15
%obsolete python2-pycdlib 1.7.0-2
%obsolete python2-pycha 0.7.0-10
%obsolete python2-pydenticon 0.3.1-5
%obsolete python2-pydocstyle 2.0.0-7
%obsolete python2-pydot 1.0.28-20
%obsolete python2-pydotplus 2.0.2-10
%obsolete python2-pyemd 0.5.1-2
%obsolete python2-pyephem 3.7.6.0-13
%obsolete python2-pyface 6.0.0-2
%obsolete python2-pyftpdlib 1.5.4-4
%obsolete python2-pygatt 3.2.0-6
%obsolete python2-pygeoip 0.2.6-18
%obsolete python2-pyghmi 1.2.4-4
%obsolete python2-pyghmi-tests 1.2.4-4
%obsolete python2-pygiftiio 1.0.4-3
%obsolete python2-pygit2 0.27.4-2
%obsolete python2-pygithub 1.39-5
%obsolete python2-pyglet 1.3.2-4
%obsolete python2-pygments-markdown-lexer 0.1.0.dev39-12
%obsolete python2-pygments-style-solarized 0.1.1-6
%obsolete python2-pygraphviz 1.5-3
%obsolete python2-pyinsane2 2.0.13-2
%obsolete python2-pyjnius 1.1.1-7
%obsolete python2-pyjokes 0.5.0-10
%obsolete python2-pykalman 0.9.5-21
%obsolete python2-pyke 1.1.1-28
%obsolete python2-pykka 1.2.1-13
%obsolete python2-pykmip 0.5.0-8
%obsolete python2-pylcdsysinfo 0-0.25
%obsolete python2-pylons 1.0.1-12
%obsolete python2-pylons-sphinx-themes 1.0.6-5
%obsolete python2-pymacaroons-pynacl 0.9.3-6
%obsolete python2-pymatreader 0.0.17-2
%obsolete python2-pymediainfo 4.1-2
%obsolete python2-pymemcache 1.2.5-15
%obsolete python2-pymoc 0.5.0-9
%obsolete python2-pymod2pkg 0.14.0-2
%obsolete python2-pymodbus 1.5.1-4
%obsolete python2-pymongo 3.7.2-2
%obsolete python2-pymongo-gridfs 3.7.2-2
%obsolete python2-pymssql 2.1.4-2
%obsolete python2-pyngus 2.3.0-2
%obsolete python2-pyodbc 3.0.10-17
%obsolete python2-pyoptical 0.4-11
%obsolete python2-pyowm 2.6.1-6
%obsolete python2-pyphen 0.9.1-15
%obsolete python2-pypng 0.0.18-13
%obsolete python2-pyprocdev 0.2-9
%obsolete python2-pyqtrailer 0.6.2-18
%obsolete python2-pyrad 2.0-17
%obsolete python2-pyramid-chameleon 0.1-16
%obsolete python2-pyramid-fas-openid 0.3.9-6
%obsolete python2-pyrax 1.9.7-8
%obsolete python2-pyrfc3339 1.0-12
%obsolete python2-pyriemann 0.2.4-6
%obsolete python2-pyro 4.71-5
%obsolete python2-pyrpmmd 0.1.1-5
%obsolete python2-pyrsistent 0.14.2-6
%obsolete python2-pyrss2gen 1.1-19
%obsolete python2-pysaml2 4.5.0-5
%obsolete python2-pysb 1.0.1-12
%obsolete python2-pyscard 1.9.5-10
%obsolete python2-pyshp 1.2.12-6
%obsolete python2-pysnmp 4.4.5-2
%obsolete python2-pyspf 2.0.12-9
%obsolete python2-pysrt 1.1.1-7
%obsolete python2-pystray 0.14.3-7
%obsolete python2-pyswip 0.2.7-4
%obsolete python2-pytelegrambotapi 3.6.6-2
%obsolete python2-pytest-beakerlib 0.7.1-7
%obsolete python2-pytest-benchmark 3.1.1-7
%obsolete python2-pytest-capturelog 0.7-14
%obsolete python2-pytest-faulthandler 1.5.0-4
%obsolete python2-pytest-spec 1.1.0-8
%obsolete python2-pytimeparse 1.1.5-14
%obsolete python2-pytorctl 0-0.25
%obsolete python2-pytrailer 0.6.1-10
%obsolete python2-pyvfs 0.2.10-11
%obsolete python2-pyvmomi 6.5-10
%obsolete python2-pyvo 0.9.2-2
%obsolete python2-pywebdav 0.9.10-8
%obsolete python2-pywt 0.5.2-10
%obsolete python2-pyxid 1.1-0.10
%obsolete python2-pyxs 0.4.1-5
%obsolete python2-pyzabbix 0.7.4-4
%obsolete python2-pyzolib 0.3.3-13
%obsolete python2-qalsadi 0.1-12
%obsolete python2-qserve 0.2.8-14
%obsolete python2-quantities 0.12.2-3
%obsolete python2-queuelib 1.4.2-10
%obsolete python2-rarfile 3.0-7
%obsolete python2-rasterio 1.0.22-2
%obsolete python2-rauth 0.7.3-6
%obsolete python2-rcssmin 1.0.6-14
%obsolete python2-rdopkg 0.51.1-2
%obsolete python2-readme_renderer 24.0-3
%obsolete python2-rebulk 0.9.0-7
%obsolete python2-recaptcha-client 2.0.1-3
%obsolete python2-recommonmark 0.4.0-17
%obsolete python2-relatorio 0.6.3-11
%obsolete python2-remctl 3.15-2
%obsolete python2-remoto 1.0.0-2
%obsolete python2-renderspec 1.7.0-7
%obsolete python2-repoze-sphinx-autointerface 0.8-10
%obsolete python2-repoze-tm2 2.0-14
%obsolete python2-repoze-what 1.0.9-21
%obsolete python2-repoze-what-plugins-sql 1.0.1-18
%obsolete python2-repoze-what-quickstart 1.0.9-18
%obsolete python2-repoze-who 2.1-16
%obsolete python2-repoze-who-friendlyform 1.0.8-19
%obsolete python2-repoze-who-plugins-sa 1.0.1-21
%obsolete python2-repoze-who-testutil 1.0.1-17
%obsolete python2-represent 1.5.1-10
%obsolete python2-reproject 0.4-5
%obsolete python2-requests-file 1.4.3-9
%obsolete python2-requests-gssapi 1.0.0-5
%obsolete python2-requests-mock 1.5.2-2
%obsolete python2-requestsexceptions 1.3.0-6
%obsolete python2-responses 0.9.0-4
%obsolete python2-rest-client 0.3-17
%obsolete python2-restauth 0.6.1-16
%obsolete python2-restauth-common 0.6.2-16
%obsolete python2-restructuredtext-lint 1.1.3-4
%obsolete python2-restsh 0.2-9
%obsolete python2-resultsdb_api 2.1.3-2
%obsolete python2-retrying 1.2.3-17
%obsolete python2-retryz 0.1.9-6
%obsolete python2-rfc3986 0.3.1-10
%obsolete python2-rfc3987 1.3.7-8
%obsolete python2-rhnlib 2.8.11-3
%obsolete python2-ripe-atlas-cousteau 1.3-9
%obsolete python2-ripe-atlas-sagan 1.1.11-10
%obsolete python2-rjsmin 1.0.12-13
%obsolete python2-rmtest 1.0.0-2
%obsolete python2-rope 0.11.0-2
%obsolete python2-ropemacs 0.7-14
%obsolete python2-ropemode 0.2-12
%obsolete python2-rows 0.3.1-8
%obsolete python2-rpdb 0.1.6-10
%obsolete python2-rpmdeplint 1.4-10
%obsolete python2-rpmfluff 0.5.6-2
%obsolete python2-rsd-lib 0.1.1-7
%obsolete python2-rsd-lib-tests 0.1.1-7
%obsolete python2-rsdclient 0.1.1-6
%obsolete python2-rsdclient-tests 0.1.1-6
%obsolete python2-rsslib 0-14
%obsolete python2-rstcheck 3.1-8
%obsolete python2-rtkit 0.6.0-12
%obsolete python2-rtree 0.8.3-8
%obsolete python2-ruamel-ordereddict 0.4.9-10
%obsolete python2-ruamel-yaml 0.15.41-3
%obsolete python2-rxjson 0.2-15
%obsolete python2-s3transfer 0.1.13-3
%obsolete python2-saharaclient 1.5.0-2
%obsolete python2-sanction 0.3.1-17
%obsolete python2-schedutils 0.6-5
%obsolete python2-schema 0.6.8-2
%obsolete python2-scp 0.10.2-11
%obsolete python2-scrapy 1.5.1-2
%obsolete python2-scriptaculous 1.8.2-21
%obsolete python2-seaborn 0.9.0-2
%obsolete python2-seesaw 0.10.0-4
%obsolete python2-selenium 3.12.0-4
%obsolete python2-semantic_version 2.6.0-8
%obsolete python2-sendgrid 3.6.5-7
%obsolete python2-sep 1.0.3-4
%obsolete python2-setuptools_hg 0.4-8
%obsolete python2-setuptools_scm_git_archive 1.0-6
%obsolete python2-shade 1.27.1-2
%obsolete python2-shadowsocks 2.9.1-7
%obsolete python2-shortuuid 0.5.0-7
%obsolete python2-shove 0.6.4-12
%obsolete python2-sievelib 1.1.1-4
%obsolete python2-signalfd 0.1-20
%obsolete python2-signedjson 1.0.0-9
%obsolete python2-simplebayes 1.5.8-5
%obsolete python2-simpleeval 0.9.6-2
%obsolete python2-simplegeneric 0.8.1-11
%obsolete python2-simpleparse 2.2.0-5
%obsolete python2-simplepath 0.3.4-7
%obsolete python2-simplewrap 0.3.3-2
%obsolete python2-simpy 3.0.9-10
%obsolete python2-slackclient 1.2.1-4
%obsolete python2-slowaes 0.1a1-11
%obsolete python2-slugify 1.2.6-2
%obsolete python2-snuggs 1.4.7-2
%obsolete python2-soaplib 0.8.1-20
%obsolete python2-social-auth 0.3.3-9
%obsolete python2-socketIO-client 0.7.2-2
%obsolete python2-sockjs-tornado 1.0.3-10
%obsolete python2-socksipy 1.00-19
%obsolete python2-softlayer 5.3.2-7
%obsolete python2-solv 0.7.5-2
%obsolete python2-sortedcontainers 2.1.0-2
%obsolete python2-speedometer 2.8-6
%obsolete python2-sphinx-argparse 0.2.2-4
%obsolete python2-sphinx-autobuild 0.7.1-11
%obsolete python2-sphinx-bootstrap-theme 0.4.13-10
%obsolete python2-sphinx-gallery 0.1.13-5
%obsolete python2-sphinx-theme-py3doc-enhanced 2.3.2-11
%obsolete python2-sphinxcontrib-actdiag 0.8.5-6
%obsolete python2-sphinxcontrib-adadomain 0.2-6
%obsolete python2-sphinxcontrib-apidoc 0.2.1-9
%obsolete python2-sphinxcontrib-autoprogram 0.1.5-5
%obsolete python2-sphinxcontrib-bibtex 0.4.0-4
%obsolete python2-sphinxcontrib-blockdiag 1.5.5-9
%obsolete python2-sphinxcontrib-cheeseshop 0.2-11
%obsolete python2-sphinxcontrib-fulltoc 1.2-8
%obsolete python2-sphinxcontrib-issuetracker 0.11-15
%obsolete python2-sphinxcontrib-pecanwsme 0.9.0-2
%obsolete python2-sphinxcontrib-programoutput 0.11-5
%obsolete python2-sphinxcontrib-seqdiag 0.8.4-16
%obsolete python2-sphinxcontrib-spelling 4.2.0-2
%obsolete python2-spiffgtkwidgets 0.2.0-15
%obsolete python2-sprox 0.10.2-6
%obsolete python2-spur 0.3.17-9
%obsolete python2-spyder 3.3.1-4
%obsolete python2-spyder-kernels 1:0.2.4-3
%obsolete python2-sql 0.9-7
%obsolete python2-sqlalchemy-collectd 0.0.3-4
%obsolete python2-sqlalchemy_schemadisplay 1.3-6
%obsolete python2-sqlite3dbm 0.1.4-15
%obsolete python2-sqlparse 0.2.4-4
%obsolete python2-sseclient 0.0.18-5
%obsolete python2-sss 2.2.2-4
%obsolete python2-sss-murmur 2.2.2-4
%obsolete python2-sssdconfig 2.2.2-4
%obsolete python2-statsd 3.2.1-12
%obsolete python2-statsmodels 0.9.0-4
%obsolete python2-stdnum 1.3-10
%obsolete python2-stem 1.7.1-2
%obsolete python2-streamlink 1.3.0-2
%obsolete python2-structlog 18.1.0-3
%obsolete python2-stuf 0.9.16-16
%obsolete python2-subliminal 2.0.5-9
%obsolete python2-subscription-manager-rhsm 1.25.9-2
%obsolete python2-subunit2sql-graph 1.9.0-2
%obsolete python2-supersmoother 0.4-7
%obsolete python2-sushy 1.3.3-2
%obsolete python2-sushy-tests 1.3.3-2
%obsolete python2-svg-path 2.2-9
%obsolete python2-sync2jira 1.7-8
%obsolete python2-sysv_ipc 0.7.0-12
%obsolete python2-tablib 0.12.1-8
%obsolete python2-taboot 0.4.0-15
%obsolete python2-tabulate 0.8.3-3
%obsolete python2-tackerclient-tests-unit 0.11.0-2
%obsolete python2-tag2distrepo 1-0.7
%obsolete python2-tambo 0.4.0-7
%obsolete python2-tashaphyne 0.2-13
%obsolete python2-taskflow 2.6.0-8
%obsolete python2-tasklib 1.1.0-6
%obsolete python2-tblib 1.5.0-2
%obsolete python2-tempdir 0.7.1-9
%obsolete python2-tenacity 4.12.0-2
%obsolete python2-termcolor 1.1.0-16
%obsolete python2-terminaltables 3.1.0-11
%obsolete python2-testinfra 1.17.0-2
%obsolete python2-testpath 0.3.1-6
%obsolete python2-textfsm 0.3.2-4
%obsolete python2-texttable 1.4.0-2
%obsolete python2-tgext-admin 0.5.4-13
%obsolete python2-tgext-crud 0.8.2-4
%obsolete python2-tgmochikit 1.4.2-19
%obsolete python2-thriftpy 0.3.9-9
%obsolete python2-tinycss 0.3-20
%obsolete python2-tinycss2 0.6.1-6
%obsolete python2-tinydb 3.10.0-2
%obsolete python2-tinyrpc 0.9.1-4
%obsolete python2-tinyrpc-tests 0.9.1-4
%obsolete python2-tld 0.7.9-9
%obsolete python2-tldextract 2.2.1-2
%obsolete python2-toml 0.10.0-2
%obsolete python2-toolz 0.9.0-6
%obsolete python2-tooz 1.48.0-8
%obsolete python2-tornadio2 0.0.4-15
%obsolete python2-tortilla 0.4.1-12
%obsolete python2-tosca-parser 0.8.1-6
%obsolete python2-toscawidgets 0.9.12-17
%obsolete python2-towncrier 17.8.0-4
%obsolete python2-tqdm 4.19.6-4
%obsolete python2-traitsui 6.0.0-2
%obsolete python2-transtats-cli 0.2.0-2
%obsolete python2-tree-format 0.1.2-4
%obsolete python2-treq 17.8.0-6
%obsolete python2-trml2pdf12 1.2-25
%obsolete python2-ttystatus 0.38-2
%obsolete python2-turbocheetah 1.0-24
%obsolete python2-turbojson 1.3.2-18
%obsolete python2-turbokid 1.0.5-19
%obsolete python2-turbomail 3.0.3-18
%obsolete python2-tw-forms 0.9.9-19
%obsolete python2-tw2-d3 0.0.8-15
%obsolete python2-tw2-jqplugins-jqplot 2.0.3-13
%obsolete python2-tw2-polymaps 0.3-13
%obsolete python2-tw2-slideymenu 2.2-13
%obsolete python2-twiggy 0.4.7-14
%obsolete python2-twilio 6.14.7-3
%obsolete python2-twitter 3.3-6
%obsolete python2-txamqp 0.8.1-7
%obsolete python2-txamqp-thrift 0.8.1-7
%obsolete python2-txredisapi 1.4.4-5
%obsolete python2-tzlocal 1.5.1-5
%obsolete python2-ucssdk 0.8.2.5-9
%obsolete python2-ufolib 2.1.1-5
%obsolete python2-unicodecsv 0.14.1-14
%obsolete python2-unicodenazi 1.1-15
%obsolete python2-unidecode 1.0.22-4
%obsolete python2-unidiff 0.5.5-6
%obsolete python2-unipath 1.1-5
%obsolete python2-units 0.07-6
%obsolete python2-unpaddedbase64 1.1.0-8
%obsolete python2-upoints 0.12.2-9
%obsolete python2-uri-templates 0.6-14
%obsolete python2-urllib-gssapi 1.0.1-5
%obsolete python2-urllib2_kerberos 0.1.6-27
%obsolete python2-usbtmc 0.8-6
%obsolete python2-v8 1:6.7.17-8
%obsolete python2-validators 0.12.0-6
%obsolete python2-vcstool 0.2.4-2
%obsolete python2-versiontools 1.9.1-19
%obsolete python2-vertica 0.8.2-2
%obsolete python2-virtualenvcontext 0.1.6-12
%obsolete python2-visionegg-quest 1.1-3
%obsolete python2-visitor 0.1.3-9
%obsolete python2-vkontakte 1.3.3-11
%obsolete python2-volume_key 0.3.12-3
%obsolete python2-vxi11 0.9-6
%obsolete python2-w3lib 1.17.0-7
%obsolete python2-walkdir 0.4.1-8
%obsolete python2-wand 0.4.4-8
%obsolete python2-weakrefmethod 1.0.2-9
%obsolete python2-weasyprint 0.22-15
%obsolete python2-webassets 0.12.1-8
%obsolete python2-webcolors 1.7-8
%obsolete python2-webpy 0.40.dev0-20170814
%obsolete python2-whichcraft 0.4.1-6
%obsolete python2-whisper 1.1.4-2
%obsolete python2-whitenoise 3.3.1-5
%obsolete python2-wikipedia 1.4.5-10
%obsolete python2-wikitools 1.3-9
%obsolete python2-windtalker 0.0.4-9
%obsolete python2-wokkel 0.7.1-14
%obsolete python2-wordpress-xmlrpc 2.3-14
%obsolete python2-wsgilog 0.3-10
%obsolete python2-wsgiproxy 0.2.2-17
%obsolete python2-wtf-peewee 0.2.6-9
%obsolete python2-www-authenticate 0.9.2-7
%obsolete python2-x2go 0.6.0.2-2
%obsolete python2-xapp 1.2.0-4
%obsolete python2-xgoogle 1.4-16
%obsolete python2-xhtml2pdf 0.1a2-11
%obsolete python2-xlrd 1.0.0-12
%obsolete python2-xml2rfc 2.5.2-8
%obsolete python2-xmlbuilder 1.0-14
%obsolete python2-xmlrunner 1.7.7-7
%obsolete python2-xmltramp 2.18-3
%obsolete python2-xnat 0.3.18-2
%obsolete python2-xunitparser 1.3.3-8
%obsolete python2-xvfbwrapper 0.2.9-5
%obsolete python2-yamlordereddictloader 0.4.0-2
%obsolete python2-yapsy 1.11.223-11
%obsolete python2-yara 3.11.0-3
%obsolete python2-yattag 1.10.0-4
%obsolete python2-yourls 0.2.0-16
%obsolete python2-yubico 1.3.2-11
%obsolete python2-zabbix-api-erigones 1.2.4-6
%obsolete python2-zake 0.2.2-13
%obsolete python2-zanata-client 1.5.2-4
%obsolete python2-zanata2fedmsg 0.2-11
%obsolete python2-zaqarclient 1.9.0-2
%obsolete python2-zbase32 1.1.5-12
%obsolete python2-zc-customdoctests 1.0.1-18
%obsolete python2-zc-lockfile 1.3.0-4
%obsolete python2-zdaemon 4.2.0-8
%obsolete python2-zict 1.0.0-2
%obsolete python2-zipstream 1.1.4-12
%obsolete python2-zope-contenttype 4.1.0-12
%obsolete python2-zope-datetime 4.1.0-10
%obsolete python2-zope-dottedname 4.1.0-13
%obsolete python2-zope-filerepresentation 4.1.0-12
%obsolete python2-zope-i18n 4.1.0-11
%obsolete python2-zope-processlifetime 2.1.0-8
%obsolete python2-zope-proxy 4.2.0-7
%obsolete python2-zope-sequencesort 4.0.1-10
%obsolete python2-zope-structuredtext 4.1.0-11
%obsolete python2-zorba 3.0.0-45
%obsolete pyutil 1.9.7-11
%obsolete pyvcs 0.2.0-16
%obsolete qmforge 2.3.2-8
%obsolete scitools 0.9.0-16
%obsolete seivot 1.18-11
%obsolete spacecmd 2.7.15-3
%obsolete statscache-plugins 0.0.2-9
%obsolete summain 0.20-9
%obsolete supernova 2.2.0-10
%obsolete synopsis 0.12-22
%obsolete synopsis-idl 0.12-22
%obsolete taboot-func 0.4.0-15
%obsolete trac-code-comments-plugin 1.2.0-0.12
%obsolete ttname 1-12
%obsolete vtk-mpich-python 7.1.1-13
%obsolete vtk-mpich-qt-python 7.1.1-13
%obsolete vtk-openmpi-python 7.1.1-13
%obsolete vtk-openmpi-qt-python 7.1.1-13

# Python 2 packages removed in Fedora 31 but never obsoleted
%obsolete ailurus 10.10.3-16
%obsolete alignak-common 1.0.0-5
%obsolete autotest-framework 0.16.2-10
%obsolete bitfrost 1.0.19-14
%obsolete bitfrost-sugar 1.0.19-14
%obsolete bitten-common 1:0.6-11
%obsolete bitten-master 1:0.6-11
%obsolete bitten-slave 1:0.6-11
%obsolete bpython 0.18-2
%obsolete cachedir 1.4-4
%obsolete carbonate 1.0.1-5
%obsolete ceph-deploy 1.5.32-9
%obsolete cherrytree 0.38.5-6
%obsolete cloudtoserver 0.2-10
%obsolete cmpi-bindings-pywbem 0.9.5-20
%obsolete cwiid-wminput 0.6.00-30
%obsolete cyphesis 0.6.2-20
%obsolete dpm-contrib-admintools 0.2.5-2
%obsolete dracut-modules-olpc 0.7.6-14
%obsolete earcandy 0.9-12
%obsolete freshmaker 0.0.4-9
%obsolete gilmsg 0.1.2-10
%obsolete gists 0.4.5-15
%obsolete gjots2 3.0.2-7
%obsolete gnome-python2 2.28.1-31
%obsolete gnome-python2-bonobo 2.28.1-31
%obsolete gnome-python2-devel 2.28.1-31
%obsolete gnome-python2-extras 2.25.3-58
%obsolete gnome-python2-libegg 2.25.3-58
%obsolete gnuplot-py 1.8-28
%obsolete gpaw-mpich 1.4.0-11
%obsolete gpaw-openmpi 1.4.0-11
%obsolete gwebsockets 0.4-12
%obsolete kf5-kross-python2 18.12.2-2
%obsolete ldtp 3.5.0-15
%obsolete mote 0.6.2-11
%obsolete openvibe 1.1.0-11
%obsolete planner 0.14.6-34
%obsolete puddletag 1.2.0-9
%obsolete pyjamas 0.7-21
%obsolete pyrenamer 0.6.0-25
%obsolete python2-GnuPGInterface 0.3.2-24
%obsolete python2-IPy 0.81-25
%obsolete python2-Levenshtein 0.12.0-10
%obsolete python2-Pyped 1.4-14
%obsolete python2-antlr 2.7.7-58
%obsolete python2-apipkg 1.5-2
%obsolete python2-argh 0.26.1-13
%obsolete python2-backports_abc 0.5-10
%obsolete python2-billiard 1:3.5.0.5-3
%obsolete python2-blessings 1.7-5
%obsolete python2-boto 2.45.0-12
%obsolete python2-cairosvg 1.0.20-11
%obsolete python2-cashe 0.99.3-10
%obsolete python2-cherrypy 3.5.0-12
%obsolete python2-cloudfiles 1.7.11-11
%obsolete python2-clustershell 1.8.3-2
%obsolete python2-collada 0.4-22
%obsolete python2-coverage-test-runner 1.15-3
%obsolete python2-cpopen 1.5-8
%obsolete python2-d2to1 0.2.12-12
%obsolete python2-dbusmock 0.18.3-3
%obsolete python2-defusedxml 0.5.0-8
%obsolete python2-dictclient 1.0.1-23
%obsolete python2-dirq 1.7.1-11
%obsolete python2-dmidecode 3.12.2-15
%obsolete python2-dockerfile-parse 0.0.11-5
%obsolete python2-dpm 1.13.0-2
%obsolete python2-dslib 3.1-13
%obsolete python2-dtopt 0.1-29
%obsolete python2-elixir 0.7.1-27
%obsolete python2-enum 0.4.4-20
%obsolete python2-execnet 1.5.0-7
%obsolete python2-eyed3 0.8-6
%obsolete python2-fabulous 0.3.0-8
%obsolete python2-fedwatch 0.5-12
%obsolete python2-flexmock 0.10.2-16
%obsolete python2-fmn-consumer 1.0.3-9
%obsolete python2-fonttools 3.38.0-2
%obsolete python2-freeradius 3.0.20-2
%obsolete python2-fudge 1.1.0-9
%obsolete python2-ganglia-gmond 3.7.2-32
%obsolete python2-genmsg 0.3.10-17
%obsolete python2-geome 2.0-13
%obsolete python2-gevent 1.3.6-3
%obsolete python2-gnupg 0.4.4-2
%obsolete python2-grabserial 1.9.9-2
%obsolete python2-grapefruit 0.1a4-11
%obsolete python2-gunicorn 19.9.0-5
%obsolete python2-h2 3.1.0-3
%obsolete python2-hgdistver 0.25-11
%obsolete python2-hglib 2.6.1-5
%obsolete python2-hl7 0.3.3-13
%obsolete python2-httpretty 0.9.5-6
%obsolete python2-imagesize 1.1.0-3
%obsolete python2-ipaddr 2.1.10-13
%obsolete python2-ipython_genutils 0.1.0-17
%obsolete python2-kazoo 2.5.0-4
%obsolete python2-kobo 0.9.0-2
%obsolete python2-kobo-client 0.9.0-2
%obsolete python2-kobo-rpmlib 0.9.0-2
%obsolete python2-kobo-worker 0.9.0-2
%obsolete python2-koji 1.20.0-2
%obsolete python2-koji-cli-plugins 1.20.0-2
%obsolete python2-lcm 1.3.1-12
%obsolete python2-lcms 1.19-27
%obsolete python2-lfc 1.13.0-2
%obsolete python2-libfdt 1.4.7-4
%obsolete python2-libhocr 0.10.17-31
%obsolete python2-libmodulemd 2.9.1-2
%obsolete python2-libopensync-plugin 1:0.22-21
%obsolete python2-libpagure 0.10-7
%obsolete python2-libselinux 2.9-5
%obsolete python2-libsemanage 2.9-3
%obsolete python2-lit 0.8.0-2
%obsolete python2-mailer 0.8.1-7
%obsolete python2-markdown2 2.3.8-2
%obsolete python2-module-build-service-copr 0.4-6
%obsolete python2-mpd2 0.5.5-11
%obsolete python2-mpmath 1.1.0-2
%obsolete python2-multi_key_dict 2.0.3-11
%obsolete python2-musicbrainz2 0.7.0-18
%obsolete python2-mysql-connector 1.1.6-16
%obsolete python2-neotime 1.0.0-5
%obsolete python2-nltk 1:3.0.3-15
%obsolete python2-nose-exclude 0.5.0-4
%obsolete python2-nose-testconfig 0.10-14
%obsolete python2-nose_fixes 1.3-8
%obsolete python2-ntlm-auth 1.1.0-5
%obsolete python2-ntlm3 1.0.2-8
%obsolete python2-oasa 0.13.1-20
%obsolete python2-oauth 1.0.1-21
%obsolete python2-odfpy 1.3.4-8
%obsolete python2-opensips 2.4.7-2
%obsolete python2-openvswitch 2.10.1-4
%obsolete python2-ordered-set 2.0.2-9
%obsolete python2-parsley 1.3-14
%obsolete python2-parso 0.5.1-3
%obsolete python2-passlib 1.7.1-3
%obsolete python2-paste-script 2.0.2-9
%obsolete python2-pathlib 1.0.1-11
%obsolete python2-pathtools 0.1.2-18
%obsolete python2-pint 0.6-17
%obsolete python2-pkgconfig 1.3.1-5
%obsolete python2-plumbum 1.6.7-2
%obsolete python2-polib 1.1.0-3
%obsolete python2-policycoreutils 2.9-5
%obsolete python2-process-tests 2.0.2-2
%obsolete python2-productmd 1.24-2
%obsolete python2-pthreading 0.1.3-14
%obsolete python2-ptrace 0.9.4-2
%obsolete python2-pycares 2.3.0-6
%obsolete python2-pycmd 1.2-16
%obsolete python2-pygal 2.4.0-7
%obsolete python2-pyhsm 1.0.4l-12
%obsolete python2-pykwalify 1.7.0-2
%obsolete python2-pylast 1.9.0-6
%obsolete python2-pyotp 2.2.7-2
%obsolete python2-pyperclip 1.6.4-3
%obsolete python2-pyramid 1.9.2-3
%obsolete python2-pyramid-mako 1.0.2-10
%obsolete python2-pyramid-tm 2.2-7
%obsolete python2-pyroute2 0.5.3-3
%obsolete python2-pysendfile 2.0.1-13
%obsolete python2-pystatgrab 0.7-14
%obsolete python2-pytest-fixture-config 1.2.11-6
%obsolete python2-pytest-flakes 4.0.0-3
%obsolete python2-rencode 1.0.6-5
%obsolete python2-retask 0.4-15
%obsolete python2-roman 3.0-3
%obsolete python2-rootplot 2.2.2-9
%obsolete python2-sane 2.8.3-11
%obsolete python2-send2trash 1.4.2-8
%obsolete python2-setools 4.1.1-15
%obsolete python2-setproctitle 1.1.10-13
%obsolete python2-setuptools_git 1.1-12
%obsolete python2-sh 1.12.14-11
%obsolete python2-simpletal 4.3-18
%obsolete python2-singledispatch 3.4.0.3-15
%obsolete python2-smmap 2.0.3-6
%obsolete python2-statistics 3.4.0-0.6
%obsolete python2-stevedore 1.30.1-6
%obsolete python2-straight-plugin 1.5.0-7
%obsolete python2-strainer 0.1.4-17
%obsolete python2-testresources 1.0.0-11
%obsolete python2-textile 3.0.4-2
%obsolete python2-tidy 0.6-2
%obsolete python2-tracing 0.9-9
%obsolete python2-txws 0.9.1-16
%obsolete python2-txzmq 0.8.0-10
%obsolete python2-uritemplate 3.0.0-6
%obsolete python2-urwid 2.0.1-5
%obsolete python2-velruse 1.1.1-13
%obsolete python2-vine 1.2.0-3
%obsolete python2-vobject 0.9.6.1-3
%obsolete python2-voluptuous 0.11.5-5
%obsolete python2-wcwidth 0.1.7-10
%obsolete python2-weberror 0.13.1-11
%obsolete python2-websockify 0.8.0-12
%obsolete python2-whoosh 2.7.4-14
%obsolete python2-wifi 0.5.0-21
%obsolete python2-woffTools 0.1-0.24
%obsolete python2-wsaccel 0.6.2-17
%obsolete python2-wsgi_intercept 1.2.2-12
%obsolete python2-xlwt 1.1.2-9
%obsolete python2-xmltodict 0.12.0-3
%obsolete python2-xtermcolor 1.3-15
%obsolete python2-yolk 0.4.3-13
%obsolete python2-zope-sqlalchemy 0.7.7-10
%obsolete python2-zsi 2.1-15
%obsolete pyttsx 1.0-16
%obsolete qmtest 2.4.1-20
%obsolete resiprocate-repro 1.10.2-27
%obsolete rho 0.0.34-4
%obsolete superkaramba-libs 15.08.3-9
%obsolete swatchbooker 0.8-0.6
%obsolete syncthing-gtk 0.9.4.4-2
%obsolete trac-fedmsg-plugin 0.4.0-11
%obsolete trac-tickettemplate-plugin 0.7-0.15
%obsolete trace-cmd-python2 2.7-5
%obsolete uwsgi-plugin-python2 2.0.17.1-8
%obsolete vegastrike 0.5.1-37
%obsolete xgridfit 2.3-7

# Python 2 packages removed in Fedora 32 but never obsoleted
%obsolete PyQt4 4.12.3-50
%obsolete PyQt4-assistant 4.12.3-50
%obsolete PyQt4-devel 4.12.3-50
%obsolete PyQt4-webkit 4.12.3-50
%obsolete PyRTF 0.45-28
%obsolete alacarte 3.11.91-15
%obsolete archmage 0.3.1-5
%obsolete audio-convert-mod 3.46.0b-19
%obsolete bacula2-client 2.4.4-34
%obsolete batti 0.3.8-19
%obsolete belier 1.2-21
%obsolete bitlyclip 0.2.2-16
%obsolete boost-mpich-python2 1.69.0-10
%obsolete boost-numpy2 1.69.0-10
%obsolete boost-openmpi-python2 1.69.0-10
%obsolete boost-python2 1.69.0-10
%obsolete bup 0.29.2-6
%obsolete cassandra-python2-cqlshlib 3.11.1-14
%obsolete certmaster 0.28-20
%obsolete chirp 20200430-2
%obsolete chm2pdf 0.9.1-26
%obsolete comedilib 0.11.0-3
%obsolete disper 0.3.1-17
%obsolete drobo-utils 0.6.2.2-28
%obsolete epydoc 3.0.1.20090203svn-13
%obsolete etckeeper-bzr 1.18.12-2
%obsolete euca2ools 3.4.1-9
%obsolete exaile 4.0.0-4
%obsolete findthatword 0.1-23
%obsolete freeorion 0.4.8-9
%obsolete func 0.30-17
%obsolete gadget 0.0.3-25
%obsolete gcc-python2-debug-plugin 0.17-5
%obsolete gcc-python2-plugin 0.17-5
%obsolete getmail 5.13-3
%obsolete gitosis 0.2-29
%obsolete glue-validator 1.0.2-19
%obsolete gnome-python2-canvas 2.28.1-31
%obsolete gnome-python2-desktop 2.32.0-39
%obsolete gnome-python2-gconf 2.28.1-31
%obsolete gnome-python2-gnome 2.28.1-31
%obsolete gnome-python2-gnomekeyring 2.32.0-39
%obsolete gnome-python2-gnomevfs 2.28.1-31
%obsolete gnome-python2-gtkspell 2.25.3-58
%obsolete gnome-python2-libwnck 2.32.0-39
%obsolete gnome-python2-rsvg 2.32.0-39
%obsolete googlecl 0.9.14-15
%obsolete gourmet 0.17.4-17
%obsolete graphviz-python2 2.40.1-55
%obsolete gresistor 0.0.2-11
%obsolete gtkparasite 0.2.0-0.10
%obsolete halberd 0.2.4-19
%obsolete hg-git 0.8.11-6
%obsolete hntool 0.1.2-21
%obsolete httpdtap 0.3-11
%obsolete jabber-roster 0.1.1-18
%obsolete k3d 0.8.0.6-25
%obsolete key-mon 1.16-14
%obsolete kross-python 4.14.3-17
%obsolete laditools 1.1.0-4
%obsolete libopensync 1:0.22-30
%obsolete mach 1.0.4-11
%obsolete marave 0.7-22
%obsolete moin 1.9.10-4
%obsolete nfspy 1.0-17
%obsolete nicotine+ 1.4.1-9
%obsolete nwsclient 1.6.4-23
%obsolete oggify 2.0.7-15
%obsolete openstv 1.7-15
%obsolete openxcap 2.2.0-4
%obsolete ovirt-engine-cli 3.6.9.2-9
%obsolete pagekite 0.5.9.3-6
%obsolete patcher 0.6-21
%obsolete pilas 1.4.7-5
%obsolete pipestat 0.4.1-18
%obsolete pius 2.2.4-7
%obsolete planet 2.0-32
%obsolete playonlinux 4.3.4-5
%obsolete postgresql-plpython2 11.7-2
%obsolete pybluez 0.22-15
%obsolete pychart 1.39-30
%obsolete pychecker 0.8.19-20
%obsolete pyexiv2 0.3.2-41
%obsolete pyifp 0.2.2-23
%obsolete pylibacl 0.5.2-13
%obsolete pyorbit 2.24.0-30
%obsolete pypoppler 0.12.2-12
%obsolete pyrit 0.5.1-0.6
%obsolete pyscript 0.6.1-25
%obsolete pysdm 0.4.1-19
%obsolete pyside-tools 0.2.13-20
%obsolete python2-Automat 0.7.0-5
%obsolete python2-Cython 0.29.13-3
%obsolete python2-GeoIP 1.3.2-13
%obsolete python2-PyPDF2 1.26.0-9
%obsolete python2-ROPGadget 5.8-2
%obsolete python2-WSGIProxy2 0.4.1-16
%obsolete python2-abiword 1:3.0.4-2
%obsolete python2-acoustid 1.1.7-3
%obsolete python2-alembic 1.1.0-2
%obsolete python2-anykeystore 0.2-23
%obsolete python2-appdirs 1.4.3-10
%obsolete python2-appindicator 12.10.0-26
%obsolete python2-application 2.1.0-7
%obsolete python2-arc 0.7.1-13
%obsolete python2-arrow 0.14.2-3
%obsolete python2-asn1crypto 0.24.0-8
%obsolete python2-atomicwrites 1.3.0-3
%obsolete python2-attrs 19.1.0-3
%obsolete python2-audioread 2.1.7-3
%obsolete python2-audit 3.0-0.16
%obsolete python2-augeas 0.5.0-16
%obsolete python2-backports 1.0-18
%obsolete python2-backports-functools_lru_cache 1.5-7
%obsolete python2-backports-ssl_match_hostname 3.5.0.1-13
%obsolete python2-bcrypt 3.1.6-4
%obsolete python2-beanbag 1.9.2-14
%obsolete python2-beautifulsoup 1:3.2.1-21
%obsolete python2-beautifulsoup4 4.9.0-2
%obsolete python2-bibtex 1.2.7-16
%obsolete python2-bitlyapi 0.1.1-21
%obsolete python2-bleach 3.1.0-3
%obsolete python2-blinker 1.4-6
%obsolete python2-blist 1.3.6-21
%obsolete python2-bottle 0.12.13-9
%obsolete python2-bunch 1.0.1-18
%obsolete python2-capstone 4.0.1-5
%obsolete python2-cassandra-driver 3.19.0-2
%obsolete python2-catkin_pkg 0.4.14-2
%obsolete python2-cddb 1.4-27
%obsolete python2-certifi 2018.10.15-6
%obsolete python2-cffi 1.12.3-2
%obsolete python2-chai 1.1.2-14
%obsolete python2-chameleon 3.6.2-3
%obsolete python2-chardet 3.0.4-11
%obsolete python2-cheetah 3.2.3-3
%obsolete python2-chm 0.8.4-27
%obsolete python2-click 7.0-5
%obsolete python2-cloudservers 1.2-19
%obsolete python2-cmdln 2.0.0-12
%obsolete python2-colorclass 2.2.0-7
%obsolete python2-condor 8.8.4-2
%obsolete python2-configobj 5.0.6-17
%obsolete python2-configparser 3.7.1-4
%obsolete python2-constantly 15.1.0-6
%obsolete python2-construct 2.9.45-4
%obsolete python2-contextlib2 0.5.5-10
%obsolete python2-coverage 4.5.4-3
%obsolete python2-crypto 2.6.1-28
%obsolete python2-cryptography 2.6.1-4
%obsolete python2-cryptography-vectors 2.6.1-3
%obsolete python2-cssselect 0.9.2-12
%obsolete python2-cssutils 1.0.2-4
%obsolete python2-cycler 0.10.0-11
%obsolete python2-daemon 2.2.3-4
%obsolete python2-dateutil 1:2.8.0-4
%obsolete python2-dbus 1.2.8-7
%obsolete python2-decorator 4.4.0-3
%obsolete python2-demjson 2.2.4-13
%obsolete python2-distutils-extra 2.39-17
%obsolete python2-django1.11 1.11.22-3
%obsolete python2-dmlite 1.13.1-3
%obsolete python2-docopt 0.6.2-13
%obsolete python2-dogpile-cache 0.6.8-3
%obsolete python2-dpath 1.4.0-15
%obsolete python2-dpkt 1.9.1-9
%obsolete python2-dulwich 0.19.12-2
%obsolete python2-easygui 0.96-26
%obsolete python2-editor 1.0.4-3
%obsolete python2-elements 0.13-21
%obsolete python2-empy 3.3.4-3
%obsolete python2-enchant 2.0.0-9
%obsolete python2-enum34 1.1.6-10
%obsolete python2-ethtool 0.14-4
%obsolete python2-eventlet 0.25.0-3
%obsolete python2-exif 2.2.0-2
%obsolete python2-extras 1.0.0-8
%obsolete python2-fasteners 0.14.1-17
%obsolete python2-fedora 0.10.0-11
%obsolete python2-fedora-flask 0.10.0-11
%obsolete python2-feedparser 5.2.1-11
%obsolete python2-fixtures 3.0.0-14
%obsolete python2-flask-babel 0.11.2-6
%obsolete python2-flask-migrate 2.1.1-6
%obsolete python2-flask-script 2.0.6-5
%obsolete python2-flask-sqlalchemy 2.4.0-3
%obsolete python2-flask-wtf 0.14.2-6
%obsolete python2-fluidity-sm 0.2.0-15
%obsolete python2-flup 1.0.3-2
%obsolete python2-formencode 1.3.1-8
%obsolete python2-freezegun 0.3.12-3
%obsolete python2-funcsigs 1.0.2-14
%obsolete python2-fuse 0.2.1-26
%obsolete python2-futures 3.3.0-2
%obsolete python2-gammu 2.12-3
%obsolete python2-gattlib 0.20150805-11
%obsolete python2-gdata 2.0.18-15
%obsolete python2-gfal2 1.9.5-4
%obsolete python2-gflags 2.0-18
%obsolete python2-gnutls 3.1.1-7
%obsolete python2-gobject 3.34.0-4
%obsolete python2-gobject-base 3.34.0-4
%obsolete python2-google-apputils 0.4.2-17
%obsolete python2-graphviz 1:0.13.2-2
%obsolete python2-greenlet 0.4.14-4
%obsolete python2-gssapi 1.6.1-2
%obsolete python2-gstreamer 0.10.22-22
%obsolete python2-gstreamer1 1.16.2-2
%obsolete python2-gtkextra 1.1.0-38
%obsolete python2-gwebsockets 0.6-2
%obsolete python2-hamcrest 1.9.0-10
%obsolete python2-hippo-canvas 0.3.0-30
%obsolete python2-hpack 3.0.0-7
%obsolete python2-html5-parser 0.4.8-2
%obsolete python2-html5lib 1:1.0.1-5
%obsolete python2-http-parser 0.8.3-22
%obsolete python2-humblewx 0.2.1-11
%obsolete python2-hupper 1.8.1-3
%obsolete python2-hyperframe 5.2.0-3
%obsolete python2-hyperlink 19.0.0-3
%obsolete python2-hypothesis 4.23.8-3
%obsolete python2-icalendar 4.0.3-4
%obsolete python2-idna 2.8-3
%obsolete python2-igraph 0.7.1.post6-15
%obsolete python2-impacket 0.9.20-2
%obsolete python2-incremental 17.5.0-7
%obsolete python2-iniparse 0.4-35
%obsolete python2-inotify 0.9.6-17
%obsolete python2-ioprocess 1.1.0-4
%obsolete python2-ipaddress 1.0.18-8
%obsolete python2-iso8601 0.1.11-14
%obsolete python2-isodate 0.6.0-3
%obsolete python2-itsdangerous 0.24-18
%obsolete python2-jenkinsapi 0.2.29-12
%obsolete python2-jsonpickle 1.1-3
%obsolete python2-jsonpointer 1.10-17
%obsolete python2-junitxml 0.7-19
%obsolete python2-jwcrypto 0.6.0-4
%obsolete python2-jwt 1.7.1-4
%obsolete python2-kajiki 0.8.0-3
%obsolete python2-kerberos 1.3.0-6
%obsolete python2-kitchen 1.2.6-3
%obsolete python2-kiwi-gtk 1.11.1-6
%obsolete python2-kiwisolver 1.1.0-3
%obsolete python2-krbv 1.0.90-23
%obsolete python2-lash 0.5.4-40
%obsolete python2-lasso 2.6.0-19
%obsolete python2-ldap 3.1.0-6
%obsolete python2-ldap3 2.6.1-2
%obsolete python2-lexicon 1.0.0-7
%obsolete python2-libcloud 2.2.1-11
%obsolete python2-libuser 0.62-22
%obsolete python2-libxml2 2.9.10-4
%obsolete python2-linecache2 1.0.0-20
%obsolete python2-lockfile 1:0.11.0-15
%obsolete python2-lxml 4.4.0-2
%obsolete python2-m2crypto 0.35.2-3
%obsolete python2-m2ext 0.1-22
%obsolete python2-m2r 0.2.0-4
%obsolete python2-magic 5.37-9
%obsolete python2-matplotlib 2.2.5-2
%obsolete python2-matplotlib-tk 2.2.5-2
%obsolete python2-matplotlib-wx 2.2.5-2
%obsolete python2-mb 2.18.1-27
%obsolete python2-mecab 0.996-2
%obsolete python2-mechanize 0.4.2-4
%obsolete python2-memcached 1.58-10
%obsolete python2-mimeparse 1.6.0-10
%obsolete python2-minibelt 0.1.1-13
%obsolete python2-miniupnpc 2.1-3
%obsolete python2-mistune 0.8.3-8
%obsolete python2-mock 3.0.5-3
%obsolete python2-mod_wsgi 4.6.6-3
%obsolete python2-modestmaps 1.4.7-4
%obsolete python2-moksha-common 1.2.5-12
%obsolete python2-monotonic 1.5-4
%obsolete python2-more-itertools 5.0.0-3
%obsolete python2-mox 0.5.3-20
%obsolete python2-mpich 3.3.2-2
%obsolete python2-msgpack 0.6.1-4
%obsolete python2-munch 2.3.2-5
%obsolete python2-musicbrainzngs 0.5-16
%obsolete python2-mysql 1.3.14-2
%obsolete python2-mysql-debug 1.3.14-2
%obsolete python2-netaddr 0.7.19-18
%obsolete python2-netifaces 0.10.6-8
%obsolete python2-newt 0.52.21-3
%obsolete python2-ngram 3.3.2-3
%obsolete python2-nine 0.3.4-19
%obsolete python2-nitrate 1.5-5
%obsolete python2-nose 1.3.7-25
%obsolete python2-notify 0.1.1-43
%obsolete python2-oauth2client 4.1.3-4
%obsolete python2-oauthlib 3.0.2-3
%obsolete python2-oletools 0.54.2-3
%obsolete python2-olpcgames 1.6-22
%obsolete python2-openid 2.2.5-22
%obsolete python2-openid-cla 1.2-13
%obsolete python2-openid-teams 1.1-16
%obsolete python2-openidc-client 0.6.0-6
%obsolete python2-openmpi 4.0.2-2
%obsolete python2-ovirt-engine-sdk 3.6.9.1-10
%obsolete python2-packaging 19.0-3
%obsolete python2-pam 1.8.4-4
%obsolete python2-paramiko 2.6.0-3
%obsolete python2-paste 3.2.2-2
%obsolete python2-paste-deploy 2.0.1-3
%obsolete python2-path 5.2-18
%obsolete python2-pathlib2 2.3.4-3
%obsolete python2-pbr 5.1.2-5
%obsolete python2-pcapy 0.11.5-3
%obsolete python2-pdc-client 1.8.0-18
%obsolete python2-pdfrw 0.4-7
%obsolete python2-pexpect 4.7.0-3
%obsolete python2-pika 1.0.1-5
%obsolete python2-pip 19.1.1-8
%obsolete python2-pkginfo 1.4.2-6
%obsolete python2-plaster 0.5-8
%obsolete python2-plaster-pastedeploy 0.7-3
%obsolete python2-pluggy 0.11.0-4
%obsolete python2-ply 3.11-4
%obsolete python2-pology 0.12-11
%obsolete python2-powerpc-utils 1.2.1-20
%obsolete python2-pp 1.6.0-19
%obsolete python2-pretend 1.0.8-17
%obsolete python2-prettytable 0.7.2-19
%obsolete python2-priority 1.3.0-7
%obsolete python2-progressbar 2.3-17
%obsolete python2-protobuf 3.6.1-6
%obsolete python2-psycopg2 2.7.7-4
%obsolete python2-psycopg2-debug 2.7.7-4
%obsolete python2-psycopg2-tests 2.7.7-4
%obsolete python2-ptyprocess 0.6.0-7
%obsolete python2-py 1.8.0-3
%obsolete python2-pyOpenSSL 19.0.0-3
%obsolete python2-pyasn1 0.4.4-6
%obsolete python2-pyasn1-modules 0.4.4-6
%obsolete python2-pyatspi 2.34.0-2
%obsolete python2-pybox2d 2.3.2-9
%obsolete python2-pycodestyle 2.5.0-4
%obsolete python2-pycparser 2.14-21
%obsolete python2-pycscope 1.2.1-20
%obsolete python2-pycurl 7.43.0.2-8
%obsolete python2-pycxx-devel 7.1.3-3
%obsolete python2-pydasm 1.6-7
%obsolete python2-pydispatcher 2.0.5-8
%obsolete python2-pydns 2.3.6-14
%obsolete python2-pyelftools 0.25-4
%obsolete python2-pyflakes 2.1.1-3
%obsolete python2-pygame 1.9.6-2
%obsolete python2-pygments 2.4.2-3
%obsolete python2-pygresql 5.1-2
%obsolete python2-pymilter 1.0.4-3
%obsolete python2-pynacl 1.3.0-3
%obsolete python2-pyobd 0.9.3-18
%obsolete python2-pyopengl 3.1.1a1-18
%obsolete python2-pypandoc 1.4-10
%obsolete python2-pyparsing 2.4.0-3
%obsolete python2-pyparted 1:3.11.2-3
%obsolete python2-pyqt4-sip 4.19.19-2
%obsolete python2-pyqt5-sip 4.19.19-2
%obsolete python2-pyquery 1.4.0-4
%obsolete python2-pyrtlsdr 0.2.8-6
%obsolete python2-pyserial 3.4-4
%obsolete python2-pyside 1.2.4-11
%obsolete python2-pysmell 0.7.3-15
%obsolete python2-pysocks 1.7.0-3
%obsolete python2-pystache 0.5.4-13
%obsolete python2-pysvn 1.9.11-3
%obsolete python2-pytest 4.4.1-5
%obsolete python2-pytest-cov 2.7.1-4
%obsolete python2-pytest-mock 1.10.4-5
%obsolete python2-pytest-relaxed 1.1.5-3
%obsolete python2-pytest-runner 4.0-6
%obsolete python2-pyusb 1.0.2-4
%obsolete python2-pyxattr 0.6.1-3
%obsolete python2-pyxdg 0.26-6
%obsolete python2-pyyaml 5.3-4
%obsolete python2-q 2.6-13
%obsolete python2-qpid 1.37.0-9
%obsolete python2-qpid-messaging 1.39.0-6
%obsolete python2-qpid-proton 0.30.0-2
%obsolete python2-qpid-qmf 1.39.0-6
%obsolete python2-qscintilla 2.11.2-5
%obsolete python2-qscintilla-qt5 2.11.2-5
%obsolete python2-qt5 5.13.2-4
%obsolete python2-qt5-base 5.13.2-4
%obsolete python2-qt5-webkit 5.13.2-4
%obsolete python2-rdflib 4.2.1-12
%obsolete python2-redis 3.2.1-3
%obsolete python2-regex 2020.2.20-2
%obsolete python2-reportlab 3.5.34-3
%obsolete python2-repoze-lru 0.7-4
%obsolete python2-requestbuilder 0.7.1-10
%obsolete python2-requests 2.22.0-4
%obsolete python2-requests-cache 0.5.1-2
%obsolete python2-requests-kerberos 0.12.0-7
%obsolete python2-requests-oauthlib 1.2.0-3
%obsolete python2-restkit 4.2.2-15
%obsolete python2-rosdep 0.17.1-2
%obsolete python2-rosdistro 0.7.5-2
%obsolete python2-rosinstall_generator 0.1.18-2
%obsolete python2-rrdtool 1.7.2-4
%obsolete python2-rsa 3.4.2-11
%obsolete python2-salttesting 2015.7.10-12
%obsolete python2-saslwrapper 0.16-24
%obsolete python2-scales 1.0.5-19
%obsolete python2-scandir 1.9.0-7
%obsolete python2-scapy 2.4.3-2
%obsolete python2-scipy 1.2.1-6
%obsolete python2-scons 3.1.2-2
%obsolete python2-scour 0.37-3
%obsolete python2-scripttest 1.3.0-17
%obsolete python2-service-identity 18.1.0-4
%obsolete python2-setuptools_scm 3.3.3-3
%obsolete python2-sexy 0.1.9-33
%obsolete python2-sieve 0.1.9-15
%obsolete python2-simplejson 3.16.0-4
%obsolete python2-simplevisor 1.2-15
%obsolete python2-sip-devel 4.19.19-2
%obsolete python2-sippy 1.1.0-0.3
%obsolete python2-skf 2.10.12-2
%obsolete python2-socketpool 0.5.3-16
%obsolete python2-socksipychain 2.0.15-7
%obsolete python2-soupsieve 1.9.2-3
%obsolete python2-sparklines 0.9-15
%obsolete python2-speaklater 1.3-17
%obsolete python2-speedtest-cli 1.0.2-9
%obsolete python2-sqlalchemy 1.3.13-2
%obsolete python2-sqlobject 3.3.0-8
%obsolete python2-staplelib 0.3.3-16
%obsolete python2-subprocess32 3.2.6-17
%obsolete python2-subunit 1.3.0-12
%obsolete python2-subversion 1.12.2-4
%obsolete python2-suds 0.7-0.14
%obsolete python2-sudsds 1.0.1-16
%obsolete python2-sure 1.4.11-7
%obsolete python2-svg 0.2.2b-20
%obsolete python2-systemd 234-10
%obsolete python2-systemd-coredump 2-9
%obsolete python2-tbgrep 0.3.0-18
%obsolete python2-telepathy 0.15.19-21
%obsolete python2-tempita 0.5.1-24
%obsolete python2-testscenarios 0.5.0-16
%obsolete python2-testtools 2.3.0-12
%obsolete python2-tftpy 0.8.0-3
%obsolete python2-tilestache 1.49.11-15
%obsolete python2-tpg 3.2.2-10
%obsolete python2-traceback2 1.4.0-21
%obsolete python2-transaction 2.4.0-4
%obsolete python2-translationstring 1.3-11
%obsolete python2-tw2-core 2.2.6-3
%obsolete python2-twisted 19.2.1-10
%obsolete python2-ujson 2.0-0.2
%obsolete python2-unicorn 1.0.1-6
%obsolete python2-unittest2 1.1.0-19
%obsolete python2-urlgrabber 4.0.0-5
%obsolete python2-urllib3 1.25.7-2
%obsolete python2-utmp 0.8.2-9
%obsolete python2-vcrpy 1.13.0-4
%obsolete python2-vcstools 0.1.42-2
%obsolete python2-venusian 1.2.0-3
%obsolete python2-visvis 1.11.2-3
%obsolete python2-volatility 2.6.1-3
%obsolete python2-vulture 0.27-6
%obsolete python2-waitress 1.2.1-4
%obsolete python2-webencodings 0.5.1-9
%obsolete python2-webob 1.8.5-3
%obsolete python2-webtest 2.0.33-3
%obsolete python2-werkzeug 0.14.1-11
%obsolete python2-wheel 1:0.33.1-4
%obsolete python2-which 1.1.0-25
%obsolete python2-wrapt 1.11.2-3
%obsolete python2-wstool 0.1.18-2
%obsolete python2-wtforms 2.2.1-6
%obsolete python2-wx-siplib 4.19.19-2
%obsolete python2-wxpython 3.0.2.0-27
%obsolete python2-wxpython-webview 3.0.2.0-27
%obsolete python2-wxpython4 4.0.6-9
%obsolete python2-wxpython4-media 4.0.6-9
%obsolete python2-wxpython4-webview 4.0.6-9
%obsolete python2-xapian 1.4.13-2
%obsolete python2-xlib 0.26-2
%obsolete python2-xmpp 0.5.0-0.23
%obsolete python2-xunitmerge 1.0.4-10
%obsolete python2-zc-buildout 2.5.3-12
%obsolete python2-zmq 18.0.2-3
%obsolete python2-zmq-tests 18.0.2-3
%obsolete python2-zope-component 4.3.0-10
%obsolete python2-zope-configuration 4.0.3-17
%obsolete python2-zope-deprecation 4.4.0-4
%obsolete python2-zope-event 4.2.0-14
%obsolete python2-zope-exceptions 4.0.8-14
%obsolete python2-zope-i18nmessageid 4.0.3-16
%obsolete python2-zope-interface 4.6.0-3
%obsolete python2-zope-schema 4.4.2-15
%obsolete python2-zope-testing 4.6.1-10
%obsolete qpid-qmf-devel 1.39.0-6
%obsolete qpid-tests 1.37.0-9
%obsolete qpid-tools 1.39.0-6
%obsolete radiotray 0.7.3-15
%obsolete rawdog 2.20-12
%obsolete rocket-depot 1.0.0-10
%obsolete shcov 5-20
%obsolete shedskin 0.9.4-12
%obsolete shiboken-python2-libs 1.2.4-15
%obsolete sidc-gui 0.4-15
%obsolete slingshot 0.9-12
%obsolete soscleaner 0.2.2-18
%obsolete sparcy 0.1-18
%obsolete sqlcli 3-16
%obsolete squeal 0.4.1-22
%obsolete subdownloader 2.0.19-11
%obsolete sugar-base 0.98.0-18
%obsolete sugar-toolkit 0.112-9
%obsolete surl 0.7.1.1-18
%obsolete svnmailer 1.0.9-17
%obsolete sx 2.17-13
%obsolete system-config-keyboard 1.4.0-19
%obsolete system-config-keyboard-base 1.4.0-19
%obsolete taskcoach 1.4.6-3
%obsolete tepache 1.1.2-16
%obsolete trac-advancedticketworkflow-plugin 0.11-17
%obsolete trac-authopenid-plugin 0.4.7-10
%obsolete trac-bazaar-plugin 0.4.2-17
%obsolete trac-doxygen-plugin 0.11.0.2-0.15
%obsolete trac-mastertickets-plugin 3.0.3-14
%obsolete trac-mercurial-plugin 1.0.0.4-9
%obsolete trac-sumfields-plugin 1.0.1-17
%obsolete trac-xmlrpc-plugin 1.2.0-0.18
%obsolete umit 1.0-17
%obsolete uniconvertor 2.0-0.20
%obsolete vhybridize 0.5.9-23
%obsolete wammu 0.44-8
%obsolete whaawmp 0.2.14-19
%obsolete winswitch 0.12.21-28
%obsolete wtop 0.6.8-16
%obsolete wxPython-devel 3.0.2.0-27
%obsolete x-tile 2.6-2
%obsolete xxdiff-tools 4.0.1-11
%obsolete zynjacku 6-26

# End Python 2

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1753069
%obsolete python3-sip 4.19.19-2

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1684162
%obsolete yum-NetworkManager-dispatcher 1.1.31-520
%obsolete yum-plugin-aliases 1.1.31-520
%obsolete yum-plugin-auto-update-debug-info 1.1.31-520
%obsolete yum-plugin-changelog 1.1.31-520
%obsolete yum-plugin-copr 1.1.31-520
%obsolete yum-plugin-fastestmirror 1.1.31-520
%obsolete yum-plugin-filter-data 1.1.31-520
%obsolete yum-plugin-fs-snapshot 1.1.31-520
%obsolete yum-plugin-keys 1.1.31-520
%obsolete yum-plugin-list-data 1.1.31-520
%obsolete yum-plugin-local 1.1.31-520
%obsolete yum-plugin-merge-conf 1.1.31-520
%obsolete yum-plugin-ovl 1.1.31-520
%obsolete yum-plugin-post-transaction-actions 1.1.31-520
%obsolete yum-plugin-priorities 1.1.31-520
%obsolete yum-plugin-protectbase 1.1.31-520
%obsolete yum-plugin-ps 1.1.31-520
%obsolete yum-plugin-puppetverify 1.1.31-520
%obsolete yum-plugin-refresh-updatesd 1.1.31-520
%obsolete yum-plugin-remove-with-leaves 1.1.31-520
%obsolete yum-plugin-rpm-warm-cache 1.1.31-520
%obsolete yum-plugin-show-leaves 1.1.31-520
%obsolete yum-plugin-tmprepo 1.1.31-520
%obsolete yum-plugin-tsflags 1.1.31-520
%obsolete yum-plugin-upgrade-helper 1.1.31-520
%obsolete yum-plugin-verify 1.1.31-520
%obsolete yum-plugin-versionlock 1.1.31-520
# we have python2-pyglet-1.3.2-3.fc29, but no python2-pyglet-1.3.2-3.fc30, use version from F31
%obsolete python-pyglet 1.4.1-1

# https://bugzilla.redhat.com/show_bug.cgi?id=1752361
%obsolete python2-pillow-tk 6.0.0-3
%obsolete python2-pillow-qt 6.0.0-3

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1750138
%obsolete python2-parsedatetime 2.4-10

%obsolete_ticket https://src.fedoraproject.org/rpms/crypto-utils/c/1dab4d23a2a59b63abe52b9650ec8679e8faf301
%obsolete crypto-utils 2.5-5

%obsolete_ticket https://src.fedoraproject.org/rpms/PyQwt/c/33ed6350df04eea7f797b3e8d96995e9c63ea135
%obsolete PyQwt 5.2.0-60

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1675241
%obsolete kupfer 208-16

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751418
%obsolete mingw64-webkitgtk 2.4.11-7
%obsolete mingw32-webkitgtk 2.4.11-7
%obsolete mingw64-webkitgtk3 2.4.11-7
%obsolete mingw32-webkitgtk3 2.4.11-7

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751419
%obsolete packagedb-cli 2.14.1-11

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751345
%obsolete nbdkit-python2-plugin 1.12.6-2

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751591
%obsolete xfce4-hamster-plugin 1.7-23

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1751913
%obsolete mono-debugger 2.10-22

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1752016
%obsolete fedora-release-notes 29-0

# Remove in F34; retired in F32+
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1578359
%obsolete python2-rabbitvcs 0.17.1-13

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1750660
%obsolete python2-libxslt 1.1.33-3

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1676261
%obsolete zanata-platform 4.6.0-3
%obsolete zanata-client 4.6.0-3
%obsolete zanata-platform-javadoc 4.6.0-3

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1755570
%obsolete maven-site-plugin 3.6-8

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1757792
%obsolete CGAL 5.0-0

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1810758
%obsolete decibel-audio-player 1.08-21

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1674704
%obsolete blueproximity 1.2.5-21

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1787079
%obsolete js-moment 2.18.1-7

%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1792929
%obsolete postgresql-plruby 0.5.7-7

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
