Name:           ember-media
Version:        0.7.2.1
# No dist tag because this is large noarch game data
Release:        11%{?dist}
Summary:        Media files for the ember WorldForge client

License:        GPLv2+ or GFDL
URL:            http://www.worldforge.org/dev/eng/clients/ember
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       ember >= 0.7.2 ember < 0.7.3 dejavu-sans-fonts
Obsoletes:      sear-media < 0.6-11

%description
Media files for the ember WorldForge client.


%prep
#FIXME
%setup -qn %{name}-0.7.2


%build
# Nothing to build!


%install
install -d $RPM_BUILD_ROOT%{_datadir}/ember/media

# In 0.5.6 media got moved to media subdir
cd media

cp -a * $RPM_BUILD_ROOT%{_datadir}/ember/media

# Remove doc files from installed media files
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/{COPYING.txt,LICENSING.txt,README}
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/user/{COPYING.txt,LICENSING.txt,README}

# Use system DejaVu fonts
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/common/themes/ember/gui/fonts/{DejaVuSans,DejaVuSans-Bold}.ttf
cd $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/common/themes/ember/gui/fonts/
ln -s ../../../../../../../../fonts/dejavu/{DejaVuSans,DejaVuSans-Bold}.ttf .
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/core/DejaVuSans.ttf
cd $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/core/
ln -s ../../../../fonts/dejavu/DejaVuSans.ttf .


%files
%doc media/shared/COPYING.txt media/shared/LICENSING.txt media/shared/core/LICENSE media/shared/core/AUTHORS
%dir %{_datadir}/ember
%{_datadir}/ember/media


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Filipe Rosset <rosset.filipe@gmail.com> - 0.7.2.1-1
- Rebuilt for new upstream release, spec cleanup, fixes rhbz #1023696

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 15 2013 Bruno Wolff III <bruno@wolff.to> - 0.7.0-3
- Move ex-sear-media users to ember-media

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Martin Preisler <mpreisle@redhat.com> - 0.7.0-1
- update to 0.7.0

* Tue Nov 13 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.3-1
- update to 0.6.3

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 Bruno Wolff III <bruno@wolff.to> - 0.6.2.1-2
- Allow a small bit of version skew between ember and ember-media

* Tue Jan 17 2012 Bruno Wolff III <bruno@wolff.to> - 0.6.2.1-1
- New upstream release 0.6.2.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 19 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.2-1
- New upstream release 0.6.2
- Release announcement: http://worldforgedev.org/archives/462

* Sun May 15 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.1-2
- Since 0.6.1-1 didn't get pushed to f15, we need to bump the release for an F16 only copy.

* Sun May 01 2011 Bruno Wolff III <bruno@wolff.to> - 0.6.1-1
- update to 0.6.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan  7 2011 Tom Callaway <spot@fedoraproject.org> - 0.6.0-1
- update to 0.6.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.6-2
- Fixing broken link to DejaVu font

* Tue Apr 28 2009 Alexey Torkhov <atorkhov@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Tue Feb 24 2009 Wart <wart@kobold.org> 0.5.5-4
- Update font package name, again.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.5-2
- Requiring correct font package

* Sat Dec 20 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.5-1
- Update to 0.5.5

* Mon Nov 03 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.4-4
- Including license text in documentation
- Fixing materials to be loadable by new OGRE

* Thu Oct 02 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.4-3
- Update for new OGRE

* Thu Sep 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.5.4-2
- use relative symlinks
- delete zero length files
- don't set files +x unnecessarily

* Tue Sep 09 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.4-1
- Update to 0.5.4.

* Tue Jul 08 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.3-1
- Update to 0.5.3.

* Fri Jun 20 2008 Alexey Torkhov <atorkhov@gmail.com> 0.5.2-1
- Inital spec for Fedora.
