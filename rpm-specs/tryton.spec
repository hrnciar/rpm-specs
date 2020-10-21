%global major 5.4

Name:           tryton
Version:        5.4.0
Release:        4%{?dist}
Summary:        Client for the Tryton application framework

License:        GPLv3+
URL:            http://www.tryton.org
Source0:        http://downloads.tryton.org/%{major}/%{name}-%{version}.tar.gz
Source1:        %{name}.1
Patch0:         %{name}-5.4.0-system.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3-sphinx


%description
This is client for the Tryton application framework. The server can be found
in the trytond package.


%prep
%setup -q
%patch0 -p1 -b .system


%build
%py3_build

pushd doc
make html SPHINXBUILD=sphinx-build-3
popd


%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_mandir}/man1/

# move data to system location
pushd %{buildroot}%{python3_sitelib}/%{name}/data
rm locale/*/*/*.po
mv locale %{buildroot}%{_datadir}/
mv pixmaps %{buildroot}%{_datadir}/
popd
rmdir %{buildroot}%{python3_sitelib}/%{name}/data

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{name}.desktop

# prepare icon pixmap
pushd %{buildroot}%{_datadir}/pixmaps
ln -sf %{name}/%{name}-icon.png %{name}-icon.png
popd

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%find_lang %{name}


%files -f %{name}.lang
%doc CHANGELOG COPYRIGHT LICENSE README.rst
%doc doc/_build/html
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.egg-info/
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}/
%{_datadir}/pixmaps/%{name}-icon.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-3
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Dan Horák <dan@danny.cz> - 5.4.0-1
- new upstream version 5.4.0 (#1751487, #1736922)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.4-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 09 2016 Dan Horák <dan@danny.cz> - 4.0.4-1
- new upstream version 4.0.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 15 2016 Dan Horák <dan@danny.cz> - 4.0.2-1
- new upstream version 4.0.2

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 14 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.6.1-2
- Remove vendor tag from desktop file

* Fri Jan 04 2013 Dan Horák <dan@danny.cz> - 2.6.1-1
- new upstream version 2.6.1

* Sat Oct 27 2012 Dan Horák <dan@danny.cz> - 2.6.0-1
- new upstream version 2.6.0

* Wed Sep 05 2012 Dan Horák <dan@danny.cz> - 2.4.1-1
- new upstream version 2.4.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Dan Horák <dan@danny.cz> - 2.4.0-1
- new upstream version 2.4.0

* Sun Jan 15 2012 Dan Horák <dan@danny.cz> - 2.2.1-1
- new upstream version 2.2.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Dan Horák <dan@danny.cz> - 2.0.2-1
- new upstream version 2.0.2

* Mon Jun 06 2011 Dan Horák <dan@danny.cz> - 2.0.1-1
- new upstream version 2.0.1

* Tue May 03 2011 Dan Horák <dan@danny.cz> - 2.0.0-1
- new upstream version 2.0.0

* Mon Feb 21 2011 Dan Horák <dan[at]danny.cz> 1.8.1-1
- update to upstream version 1.8.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Dan Horák <dan[at]danny.cz> 1.8.0-1
- update to upstream version 1.8.0

* Sat Nov 13 2010 Dan Horák <dan[at]danny.cz> 1.6.2-1
- update to upstream version 1.6.2

* Tue Oct 26 2010 Dan Horák <dan[at]danny.cz> 1.6.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 27 2010 Dan Horák <dan[at]danny.cz> 1.6.1-1
- update to upstream version 1.6.1

* Thu Jul 22 2010 Dan Horák <dan[at]danny.cz> 1.6.0-3.1
- don't build docs on EL <= 5

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jul 15 2010 Dan Horák <dan[at]danny.cz> 1.6.0-2
- build documentation
- add missing R: python-dateutil

* Wed Jul  7 2010 Dan Horák <dan[at]danny.cz> 1.6.0-1
- update to upstream version 1.6.0

* Thu Apr  1 2010 Dan Horák <dan[at]danny.cz> 1.4.3-1
- update to upstream version 1.4.3

* Fri Feb 19 2010 Dan Horák <dan[at]danny.cz> 1.4.2-1
- update to upstream version 1.4.2

* Sat Nov 28 2009 Dan Horák <dan[at]danny.cz> 1.4.1-1
- update to upstream version 1.4.1

* Wed Oct 21 2009 Dan Horák <dan[at]danny.cz> 1.4.0-1
- update to upstream version 1.4.0

* Mon Aug 31 2009 Dan Horák <dan[at]danny.cz> 1.2.2-1
- update to upstream version 1.2.2

* Wed Aug 26 2009 Dan Horák <dan[at]danny.cz> 1.2.1-3
- fixed Source0 URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Dan Horák <dan[at]danny.cz> 1.2.1-1
- update to upstream version 1.2.1

* Sat May 23 2009 Dan Horák <dan[at]danny.cz> 1.2.0-1
- update to upstream version 1.2.0
- use upstream desktop file

* Fri Mar  6 2009 Dan Horák <dan[at]danny.cz> 1.0.3-1
- update to upstream version 1.0.3

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan  7 2009 Dan Horák <dan[at]danny.cz> 1.0.2-1
- update to upstream version 1.0.2

* Mon Dec 29 2008 Dan Horák <dan[at]danny.cz> 1.0.1-2
- set vendor for the desktop file
- improve Description

* Mon Dec  1 2008 Dan Horák <dan[at]danny.cz> 1.0.1-1
- update to upstream version 1.0.1

* Fri Nov 28 2008 Dan Horák <dan[at]danny.cz> 1.0.0-1
- initial Fedora version
