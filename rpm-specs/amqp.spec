%global revision 1688630
%global date     20150701

Name:           amqp
Version:        1.0
Release:        12.%{date}svn%{revision}%{?dist}
# increase Epoch to 1 cause of modified Release logic
Epoch:          1
Summary:        The AMQP specification

# Fedora treats these files as content, not code.
# The AMQP license does not give the right to modify.
License:        ASL 2.0

URL:            http://www.amqp.org
Source0:        %{name}-%{version}-%{revision}.tar.gz
# svn export -r %{revision} http://svn.apache.org/repos/asf/qpid/trunk/qpid/specs /tmp/%{name}-%{version}
# cd /tmp ; tar czf %{name}-%{version}-%{revision}.tar.gz /tmp/%{name}-%{version}

BuildArch:      noarch
BuildRequires:  libxslt

%description
The AMQP (advanced message queuing protocol) specification in XML format.

%package devel
Summary: Development files for %{name}
# be careful with epoch!
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
%{summary}.


%prep
%setup -q

%build
find . -name \*.xml -exec xsltproc -o '{}.html' %{name}.xsl '{}' \;
rename -v '.xml' '' *.html

%install
install -d -m0755 %{buildroot}%{_datadir}/%{name}
install -p -m0644 *.xml *.dtd %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc NOTICE MOVED_FILE
%doc *.html

%files devel
%license LICENSE
%{_datadir}/%{name}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-12.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-11.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-10.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-9.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-8.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-7.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-6.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-5.20150701svn1688630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Raphael Groner <projects.rg@smart.ms> - 1:1.0-4.20150701svn1688630
- fix R: to main package (rhbz#1292308)

* Wed Jul 01 2015 Raphael Groner <projects.rg@smart.ms> - 1:1.0-3.20150701svn1688630
- revision 1688630 (rhbz#1236039)

* Wed Jun 24 2015 Raphael Groner <projects.rg@smart.ms> - 1:1.0-2.20150624svn1687244
- revision 1687244 (rhbz#1234656)
- add epoch for devel subpackage

* Mon Jun 22 2015 Raphael Groner <projects.rg@smart.ms> - 0:1.0-1.20150622svn1686756
- cleanup spec
- bump to revision 1686756 (rhbz#1234167)
- use right license
- generate html
- move sources to devel subpackage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.819819-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.819819-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.819819-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.819819-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.819819-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.819819-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.819819-1
- Rebased to svn rev 819819 for F12 beta

* Fri Sep 25 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.818599-1
- Rebased to svn rev 818599

* Fri Sep 18 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.816781-1
- Rebased to svn rev 816781

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.790661-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  2 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.790661-1
- Rebased to svn rev 790661

* Fri Jun 26 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.788782-1
- Rebased to svn rev 788782

* Mon Jun 22 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.787286-1
- Rebased to svn rev 787286

* Thu Mar 19 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.752600-1
- Rebased to svn rev 752600

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.738618-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.738618-1
- Rebased to svn rev 738618

* Wed Jan 14 2009 Nuno Santos <nsantos@redhat.com> - 0:1.0.734452-1
- Rebased to svn rev 734452

* Tue Dec 23 2008 Nuno Santos <nsantos@redhat.com> - 0:1.0.728142-2
- Rebased to svn rev 728142

* Tue Dec  2 2008 Nuno Santos <nsantos@redhat.com> - 0:1.0.722557-1
- Rebased to svn rev 722557

* Tue Nov 25 2008 Nuno Santos <nsantos@redhat.com> - 0:1.0.720585-1
- Rebased to svn rev 705858

* Thu Oct 16 2008 Nuno Santos <nsantos@redhat.com> - 0:1.0.705289-1
- Rebased to svn rev 705289

* Thu Oct  2 2008 Nuno Santos <nsantos@redhat.com> - 0:1.0.700546-1
- Rebased to svn rev 700546

* Mon Sep  8 2008 Nuno Santos <nsantos@redhat.com> - 0:1.0.693140-1
- Update for Fedora 10

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0:1.0.666398-6
- fix license tag

* Tue Jun 10 2008 Rafael Schloming <rafaels@redhat.com> - 0:1.0.666398-5
- Source update for MRG RC1

* Mon Jun  9 2008 Rafael Schloming <rafaels@redhat.com> - 0:1.0.665769-5
- Source update for MRG RC1

* Tue May 13 2008 Rafael Schloming <rafaels@redhat.com> - 0:1.0.656025-5
- Update the source tarball for MRG Beta 4

* Mon May 12 2008 Rafael Schloming <rafaels@redhat.com> - 0:1.0-5
- Imported new source tarball for MRG Beta 4

* Tue Apr 22 2008  Nuno Santos <nsantos@redhat.com> - 0:1.0-4
- Include 0-10 DTD

* Mon Nov 26 2007 Nuno Santos  <nsantos@redhat.com> - 1.0-2
- Bump release for brew update

* Wed Aug 01 2007 Nuno Santos  <nsantos@redhat.com> - 1.0-1
- Include multiple versions of the spec; bump release

* Thu Mar 22 2007 Rafael Schloming  <rafaels@redhat.com> - 0.8-2rhm.1
- Comply with Fedora packaging guidelines

* Wed Dec 20 2006 Rafael Schloming <rafaels@redhat.com> - 0.8-2rhm
- Bumped the release.

* Wed Dec 20 2006 Rafael Schloming <rafaels@redhat.com> - 0.8-1
- Initial build.
