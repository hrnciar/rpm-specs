%global modname DNS
%global distname py3dns

Name:               python3-py3dns
Version:            3.2.1
Release:            2%{?dist}
Summary:            Python3 DNS library

License:            Python
URL:                https://launchpad.net/py3dns/
Source0:            https://pypi.io/packages/source/p/%{distname}/%{distname}-%{version}.tar.gz
#Source0:            https://pypi.io/packages/source/p/%{distname}/%{distname}-%{version}.tar.gz

# At buildtime, py3dns tries to read in /etc/resolv.conf and crashes if it
# doesn't exist.  Our koji builders don't have that file.  This patch just
# avoids the crash if that file is absent.
Patch0:             python3-py3dns-handle-absent-resolv.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1561187
Patch1:             python3-py3dns-py3_friendly_warning.patch

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%description
This Python 3 module provides a DNS API for looking up DNS entries from
within Python 3 modules and applications. This module is a simple,
lightweight implementation.


%prep
%setup -q -n %{distname}-%{version}
%patch0 -p1
%patch1 -p1

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

# Some files are latin-1 encoded but are incorrectly labelled as UTF-8 by
# upstream (see rhbz:620265)
#
# Convert them to actually be UTF-8, preserving the (now-correct) encoding
# declaration (preserving timestamps):
for file in DNS/Lib.py DNS/Type.py ; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}

# We cannot actually run the tests in koji because they require network access.
#%%check
#PYTHONPATH=$(pwd) %%{__python3} tests/test.py
#PYTHONPATH=$(pwd) %%{__python3} tests/test2.py
#PYTHONPATH=$(pwd) %%{__python3} tests/test4.py
##PYTHONPATH=$(pwd) %%{__python3} tests/test5.py somedomain.com
#PYTHONPATH=$(pwd) %%{__python3} tests/testPackers.py
#PYTHONPATH=$(pwd) %%{__python3} tests/testsrv.py

%files
%doc README.txt README-guido.txt LICENSE CREDITS.txt CHANGES
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{distname}-%{version}*

%changelog
* Mon Oct  5 2020 Bojan Smojver <bojan@rexursive.com> - 3.2.1-2
- Add python3-setuptools to build requirements

* Sun Aug  2 2020 Bojan Smojver <bojan@rexursive.com> - 3.2.1-1
- Bump up to 3.2.1, bug #1862311

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-7
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Kevin Fenzi <kevin@scrye.com> - 3.1.1-6
- Add patch to change now reserved async keyword to py3async. Fixes bug #1583688

* Tue Mar 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.1.1-5
- Don't blow up in Python 3 if /etc/resolv.conf is missing (#1561187).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Ralph Bean <rbean@redhat.com> - 3.1.1-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.4-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Sep 24 2013 Ralph Bean <rbean@redhat.com> - 3.0.4-2
- Update with comments from review.

* Mon Sep 23 2013 Ralph Bean <rbean@redhat.com> - 3.0.4-1
- Initial package for Fedora
