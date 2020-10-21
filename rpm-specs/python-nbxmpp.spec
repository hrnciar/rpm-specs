%global modname nbxmpp
%global sum Python library for non-blocking use of Jabber/XMPP

Name:           python-%{modname}
Version:        1.0.0
Release:        2%{?dist}
Summary:        %{sum}
License:        GPLv3
URL:            https://dev.gajim.org/gajim/python-nbxmpp/
Source0:        https://dev.gajim.org/gajim/python-nbxmpp/-/archive/nbxmpp-%{version}/python-nbxmpp-nbxmpp-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python3-devel

%global desc python-nbxmpp is a Python library that provides a way for Python applications\
to use Jabber/XMPP networks in a non-blocking way.

%description
%{desc}

%package -n python3-%{modname}
Summary:        %{sum}
Requires:       python3-pyOpenSSL
Requires:       python3-gobject-base
Requires:       libsoup
Recommends:     python3-kerberos
Obsoletes:      python-nbxmpp-doc < 1.0.0
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
%{desc}

%prep
%autosetup -n python-nbxmpp-nbxmpp-%{version}

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{modname}
%license COPYING
%doc README.md ChangeLog nbxmpp/examples
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}-*.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Michal Schmidt <mschmidt@redhat.com> - 1.0.0-1
- Upstream release 1.0.0.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.10-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Michal Schmidt <mschmidt@redhat.com> - 0.6.10-1
- Upstream release 0.6.10.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Michal Schmidt <mschmidt@redhat.com> - 0.6.9-1
- Upstream release 0.6.9.

* Wed Nov 14 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.8-1
- Upstream release 0.6.8.

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.6-1
- Upstream release 0.6.6.

* Mon Mar 19 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.4-1
- Upstream release 0.6.4.

* Wed Mar 07 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.3-1
- Upstream release 0.6.3.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Michal Schmidt <mschmidt@redhat.com> - 0.6.2-1
- Upstream release 0.6.2.

* Mon Dec 04 2017 Michal Schmidt <mschmidt@redhat.com> - 0.6.1-1
- Upstream release 0.6.1.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Michal Schmidt <mschmidt@redhat.com> - 0.5.6-1
- Upstream release 0.5.6.

* Mon Feb 06 2017 Michal Schmidt <mschmidt@redhat.com> - 0.5.5-1
- Upstream release 0.5.5.
- New upstream location and tarball format.
- Refer to python2-kerberos using its actual package name.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 18 2016 Michal Schmidt <mschmidt@redhat.com> - 0.5.3-3
- Build as both python2-nbxmpp and python3-nbxmpp. (#1309621)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Matej Cepl <mcepl@redhat.com> - 0.5.3-1
- Upstream release 0.5.3.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Michal Schmidt <mschmidt@redhat.com> - 0.5.2-1
- Upstream bugfix release 0.5.2.

* Thu Oct 16 2014 Michal Schmidt <mschmidt@redhat.com> - 0.5.1-1
- New upstream release, required by Gajim 0.16.

* Mon Aug 11 2014 Michal Schmidt <mschmidt@redhat.com> - 0.5-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Michal Schmidt <mschmidt@redhat.com> - 0.4-1
- Initial Fedora packaging.
