Name:           lazygal
Version:        0.9.3
Release:        10%{?dist}
Summary:        A static web gallery generator

License:        GPLv2+ and MIT
URL:            https://sml.zincube.net/~niol/repositories.git/lazygal/about/
Source0:        https://sml.zincube.net/~niol/repositories.git/lazygal/snapshot/lazygal-%{version}.tar.bz2
Patch0:         lazygal-0.9.3-4f7e502.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  js-jquery
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-gexiv2
BuildRequires:  python3-genshi
BuildRequires:  python3-gstreamer1
BuildRequires:  python3-pillow
BuildRequires:  glibc-langpack-en
Recommends:     gstreamer1-plugins-base
Recommends:     gstreamer1-plugins-good
Requires:       js-jquery
Requires:       python3-gexiv2
Requires:       python3-genshi
Requires:       python3-pillow
Recommends:     python3-gstreamer1
Provides:       bundled(jquery.tipTip.js) = 1.3
Provides:       bundled(respond.js) = 1.4.2
Provides:       bundled(jquery.colorbox.js) = 1.4.36
# still bundled JS in themes/
# inverted/SHARED_plugins.tjs TipTip 1.3 https://github.com/drewwilson/TipTip
# inverted/SHARED_respond.js https://github.com/scottjehl/Respond
# singlepage/SHARED_jquery.colorbox.js Colorbox v1.4.36 - http://www.jacklmoore.com/colorbox (available via npm)

%description
Lazygal is another static web gallery generator written in Python.
It can be summed up by the following features :
* Command line based (thus scriptable).
* Handles album updates.
* Presents all your pictures and videos and associated data.
* Makes browsing sharing pictures easy.
* Make customization easy.
* Does not change your original pictures directories (the source argument).

%prep
%setup -q
%patch0 -p1

%build
%py3_build
%{__python3} setup.py build_i18n
%{__python3} setup.py build_manpages

%install
%py3_install
install -dm755 %{buildroot}%{_mandir}/man{1,5}
install -pm644 man/lazygal.1 %{buildroot}%{_mandir}/man1/
install -pm644 man/lazygal.conf.5 %{buildroot}%{_mandir}/man5/
install -dm755 %{buildroot}%{_datadir}/locale
cp -pr build/mo/* %{buildroot}%{_datadir}/locale/

%find_lang %{name}

%check
%{__python3} setup.py test

%files -f %{name}.lang
%license COPYING
%doc README.md TODO ChangeLog
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-10
- Rebuilt for Python 3.9

* Fri Apr 10 2020 Dominik Mierzejewski <rpm@greysector.net> - 0.9.3-9
- Rebase to current git HEAD to fix build with Python 3.9
- Drop obsolete patches and work-arounds
- Switch from xsltproc to pandoc
- Use modern jquery

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 0.9.3-4
- fix two test failures

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.3-2
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Nov 03 2018 Dominik Mierzejewski <rpm@greysector.net> - 0.9.3-1
- update to 0.9.3 (#1643661)
- update URLs
- use license macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-6
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-2
- Rebuild for Python 3.6

* Fri Nov 18 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.9.1-1
- update to 0.9.1 (#1390795)
- drop obsolete patches

* Fri Nov 11 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.9-2
- backport fix for bad author tag decoding test

* Fri Nov 04 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.9-1
- update to 0.9 (#1390795)
- backport a patch to use the default nojs theme
- add missing gstreamer dependencies for video processing
- switch to python3

* Mon Aug 22 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.8.8-2
- fix broken dependency after libgexiv2-python2 rename

* Fri Oct 09 2015 Dominik Mierzejewski <rpm@greysector.net> - 0.8.8-1
- update to 0.8.8
- unbundle jquery
- enable testsuite
- use new python convenience macros
- add a soft dependency on python-gstreamer1
- add required Provides: for bundled JavaScript libraries

* Wed Jul 23 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.8.4-2
- drop Group: tag
- fix manpages listing in file list

* Sun Jul 20 2014 Dominik Mierzejewski <rpm@greysector.net> - 0.8.4-1
- update to 0.8.4
- split BRs and Requires into separate lines and sort
- drop redundant specfile parts
- use python version-specific macros

* Fri Jul 30 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-6
- add patch to fix broken imports under python 2.7

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 8 2009 Byron Clark <byron@theclarkfamily.name> 0.4.1-3
- Use python-devel in place of python for BuildRequires.
- Add TODO and ChangeLog to docs.
- Add spacing to changelog entries.

* Mon May 25 2009 Byron Clark <byron@theclarkfamily.name> 0.4.1-2
- Fix typo in upstream URL.

* Sun May 24 2009 Byron Clark <byron@theclarkfamily.name> 0.4.1-1
- Initial release
