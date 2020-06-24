%global py_interp %{__python3}

Name:           mint-y-icons
Version:        1.4.3
Release:        1%{?dist}
Summary:        The Mint-Y icon theme

License:        CC-BY-SA
URL:            http://linuxmint.com
Source0:        http://packages.linuxmint.com/pool/main/m/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  python3-devel

Requires:       filesystem
Requires:       mint-x-icons
Requires:       gnome-icon-theme
Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n %{name}


%build
# Add links for some additional programs.
#pushd %%{name}
#{py_interp} ./create-links src.png dest.png
#popd


%install
#pushd %%{name}
%{__cp} -pr ${PWD}%{_prefix} %{buildroot}
%fdupes -s %{buildroot}
#popd


%transfiletriggerin -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%transfiletriggerpostun -- %{_datadir}/icons/Mint-Y
for _dir in %{_datadir}/icons/Mint-Y*/ ; do
  %{_bindir}/gtk-update-icon-cache --force ${_dir} &>/dev/null || :
done


%files
%license debian/copyright
%doc debian/changelog
%doc README.md
%{_datadir}/icons/Mint-*/


%changelog
* Thu Jun 18 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.3-1
- New upstream release

* Sat Jun 06 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.2-1
- New upstream release

* Sun May 24 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-1
- New upstream release

* Tue May 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.0-1
- New upstream release

* Tue Apr 21 2020 Leigh Scott <leigh123linux@gmail.com> - 1.3.8-1
- New upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.7-1
- New upstream release

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.6-1
- New upstream release

* Sun Nov 03 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.5-1
- New upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.3.4-1
- New upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.3-1
- New upstream release

* Tue Nov 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.2-1
- New upstream release

* Thu Aug 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.3.0-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.6-1
- New upstream release

* Thu Jun 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.5-1
- New upstream release

* Sat Jun 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.3-1
- New upstream release

* Tue May 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.1-1
- New upstream release

* Mon May 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.2.0-1
- New upstream release

* Mon May 21 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.9-1
- New upstream release

* Sun May 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.5-1
- New upstream release

* Fri Apr 27 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-1
- New upstream release

* Mon Apr 02 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-0.2.20180321git415a843
- Update to git snapshot

* Sat Feb 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-0.1.20180224git9204077
- Update to git snapshot (adds hidpi icons)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.3-2
- Use rpm filetriggers on Fedora and/or RHEL >= 8

* Fri Nov 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.3-1
- New upstream release

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-3
- Fix dir descriptions in index.theme

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-2
- Backported new action and app icons from upstream

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-1
- New upstream release (rhbz#1515227)

* Thu Nov 23 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-2
- Add explicit Requires on {gnome,hicolor}-icon-theme
- Simplify scriptlets

* Wed Nov 15 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.0-1
- New upstream release (rhbz#1512346)

* Mon Nov 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.9-1
- New upstream release (rhbz#1509754)

* Fri Sep 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-6
- Add eye-candy for online-accounts

* Sun Aug 27 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-5
- Adjustments for building on EPEL

* Sun Aug 27 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-4
- Create symlinks for modem-manager-gui

* Fri Aug 25 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-3
- Create symlinks for tilix

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.8-1
- New upstream release (rhbz#1463454)

* Wed May 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.7-1
- New upstream release (rhbz#1450541)

* Mon May 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.5-1
- New upstream release (rhbz#1448743)

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-6
- Create symlinks for additional apps with script in sources

* Sat Apr 08 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-5
- Add icons for lightdm-settings

* Sun Feb 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-4
- Fix License GPLv3+  --->  CC-BY-SA

* Sun Feb 05 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-3
- Symlink files to save disk-space

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.4-2
- Add icons for dnfdragora

* Mon Jan 09 2017 Björn Esser <bjoern.esser@gmail.com> - 1.0.4-1
- Initial rpm-release (rhbz#1411153)

* Sun Jan 08 2017 Björn Esser <bjoern.esser@gmail.com> - 1.0.4-0.1
- Initial package (rhbz#1411153)
