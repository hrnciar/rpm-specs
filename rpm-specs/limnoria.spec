# Default to python3 in f29+
%if 0%{?fedora} > 28
%global python3 1
%else
%global python3 0
%endif

%global upstreamver 2020-03-19

Name:           limnoria
Version:        20200319
Release:        2%{?dist}
Summary:        A modified version of Supybot (an IRC bot) with enhancements and bug fixes

License:        BSD and GPLv2 and GPLv2+
#
# The bulk of the package is BSD. 
# Parts of the Math plugin are GPLv2+
# The Dict plugin is GPLv2+
#
URL:            https://github.com/ProgVal/Limnoria
Source0:        https://github.com/ProgVal/Limnoria/archive/master-%{upstreamver}.tar.gz

BuildArch:      noarch

# Provide the upper case version also to avoid confusion
Provides: Limnoria = %{version}-%{release}

#
# Obsolete the supybot-gribble package as this is a newer/maintained fork.
#
Obsoletes: supybot-gribble =< 0.83.4.1-18%{dist}
Provides: supybot-gribble = 0.83.4.1-19%{dist}

%if %{python3}
BuildRequires:  python3-devel
BuildRequires:  python3-chardet
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
BuildRequires:  python3-gnupg
BuildRequires:  python3-feedparser
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pysocks
BuildRequires:  python3-mock
BuildRequires:  python3-ecdsa
Requires:  python3-devel
Requires:  python3-chardet
Requires:  python3-pytz
Requires:  python3-dateutil
Requires:  python3-gnupg
Requires:  python3-feedparser
Requires:  python3-sqlalchemy
Requires:  python3-pysocks
Requires:  python3-mock
Requires:  python3-ecdsa
%else
BuildRequires:  python2-devel
BuildRequires:  python2-chardet
BuildRequires:  python2-pytz
BuildRequires:  python2-dateutil
BuildRequires:  python2-gnupg
BuildRequires:  python2-feedparser
BuildRequires:  python2-sqlalchemy
BuildRequires:  python2-pysocks
BuildRequires:  python2-mock
BuildRequires:  python2-ecdsa
# Need to require packages for runtime as well.
Requires:  python2-devel
Requires:  python2-chardet
Requires:  python2-pytz
Requires:  python2-dateutil
Requires:  python2-gnupg
Requires:  python2-feedparser
Requires:  python2-sqlalchemy
Requires:  python2-pysocks
Requires:  python2-mock
Requires:  python2-ecdsa
%endif

%description
Supybot is a robust (it doesn't crash), user friendly 
(it's easy to configure) and programmer friendly 
(plugins are extremely easy to write) Python IRC bot.
It aims to be an adequate replacement for most existing IRC bots.
It includes a very flexible and powerful ACL system for controlling 
access to commands, as well as more than 50 builtin plugins 
providing around 400 actual commands.

Limnoria is a project which continues development of Supybot 
(you can call it a fork) by fixing bugs and adding features 
(see the list of added features for more details).

%prep
%autosetup -n Limnoria-master-%{upstreamver}

%build
# remove stray python bits from debug plugin
sed -i 1"s|#!/usr/bin/python||" plugins/Debug/plugin.py

# This should be set to the day of the release. 
# It's gets added as 'version' and is based on build time, not release time.
export SOURCE_DATE_EPOCH=1573327269

%if %{python3}
%{__python3} setup.py build
%else
%{__python2} setup.py build
%endif

%install
%if %{python3}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%else
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%endif

# TODO: get tests working
#check

%files
%doc ChangeLog CONTRIBUTING.md README.md RELNOTES
%license LICENSE.md
%{_bindir}/supybot
%{_bindir}/supybot-adduser
%{_bindir}/supybot-botchk
%{_bindir}/supybot-plugin-create
%{_bindir}/supybot-plugin-doc
%{_bindir}/supybot-test
%{_bindir}/supybot-wizard
%{_bindir}/supybot-reset-password
%{_mandir}/man1/supybot-adduser.1.gz
%{_mandir}/man1/supybot-botchk.1.gz
%{_mandir}/man1/supybot-plugin-create.1.gz
%{_mandir}/man1/supybot-plugin-doc.1.gz
%{_mandir}/man1/supybot-test.1.gz
%{_mandir}/man1/supybot-wizard.1.gz
%{_mandir}/man1/supybot.1.gz
%if %{python3}
%{python3_sitelib}/*
%else
%{python2_sitelib}/*
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20200319-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Kevin Fenzi <kevin@scrye.com> - 20200319-1
- Update to 20200319. 

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Kevin Fenzi <kevin@scrye.com> - 20191109-2
- Fix incorrect version reporting.

* Sat Nov 09 2019 Kevin Fenzi <kevin@scrye.com> - 20191109-1
- Update to 2019-11-09

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 20180625.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 20180625.2-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180625.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180625.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 02 2018 Kevin Fenzi <kevin@scrye.com> - 20180625.2-2
- Switch to python3 by default in f29+

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 20180625.2-1
- Update to 2018-06-25-2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 20171025-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Kevin Fenzi <kevin@scrye.com> - 20171025-1
- Update to 20171025.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170127-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Kevin Fenzi <kevin@scrye.com> - 20170127-1
- Update to 20170127

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20160506-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 07 2016 Kevin Fenzi <kevin@scrye.com> - 20160506-2
- Updates from review: Fixed license
- Added Run time requires for needed python packages. 

* Sat Jun 04 2016 Kevin Fenzi <kevin@scrye.com> - 20160506-1
- Initial Fedora/EPEL version
