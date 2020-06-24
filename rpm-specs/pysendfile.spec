%global srcname pysendfile
%global sum Python interface to the sendfile(2) system call

Name:           %{srcname}
Version:        2.0.1
Release:        17%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/giampaolo/pysendfile
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?filter_setup:
%filter_provides_in %{python_sitearch}
%filter_setup
}

%description
sendfile(2) is a system call which provides a "zero-copy" way of copying data
from one file descriptor to another (a socket). The phrase "zero-copy" refers
to the fact that all of the copying of data between the two descriptors is done
entirely by the kernel, with no copying of data into user-space buffers. This is
particularly useful when sending a file over a socket (e.g. FTP). 


%package -n python3-%{srcname}
Summary:  %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
sendfile(2) is a system call which provides a "zero-copy" way of copying data
from one file descriptor to another (a socket). The phrase "zero-copy" refers
to the fact that all of the copying of data between the two descriptors is done
entirely by the kernel, with no copying of data into user-space buffers. This is
particularly useful when sending a file over a socket (e.g. FTP). 
This is Python 3 version.


%prep
%setup -q


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH="$RPM_BUILD_ROOT%{python3_sitearch}" %{__python3} test/test_sendfile.py


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%attr(755, root, root) %{python3_sitearch}/sendfile.*.so
%{python3_sitearch}/pysendfile-%{version}-*.egg-info


%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-13
- Subpackage python2-pysendfile has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0.1-6
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul  5 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.1-2
- Provides/Obsoletes old name

* Wed Jun 08 2016 Dominika Krejci <dkrejci@redhat.com> - 2.0.1 - 1
- Add Python 3
- Upgrade version to 2.0.1
- Update source and URL (project moved to GitHub)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 8 2012 Russell Bryant <russellb@fedoraproject.org> - 2.0.0-3
- Update %%check section to a more sane method of setting PYTHONPATH

* Wed Feb 8 2012 Russell Bryant <russellb@fedoraproject.org> - 2.0.0-2
- Remove unnecessary cleaning of the buildroot in %%install section
- Add %%check section to run the unit tests
- Rename package from python-sendfile to pysendfile

* Tue Feb 7 2012 Russell Bryant <russellb@fedoraproject.org> - 2.0.0-1
- Initial package
