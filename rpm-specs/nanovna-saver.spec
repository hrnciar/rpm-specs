Name:		nanovna-saver
Version:	0.2.2
Release:	5%{?dist}
Summary:	Tool for reading, displaying and saving data from the NanoVNA
License:	GPLv3
URL:		https://github.com/mihtjel/%{name}

Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
# Reported upstream: https://github.com/mihtjel/nanovna-saver/issues/163
Source1:	nanovna-saver.desktop
BuildArch:	noarch
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-pyserial
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy
BuildRequires:	python3-qt5
BuildRequires:	sed
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme
# OS/distro specific
Patch0:		nanovna-saver-0.2.2-fedora-icon.patch
# https://github.com/mihtjel/nanovna-saver/pull/162
Patch1:		nanovna-saver-0.2.2-test-fix.patch

%description
A multiplatform tool to save Touchstone files from the NanoVNA, sweep
frequency spans in segments to gain more than 101 data points, and
generally display and analyze the resulting data.

%prep
%setup -q
%autopatch -p1

# Drop shebang of non-executable
sed -i '1 d' NanoVNASaver/__main__.py

%build
%py3_build

%install
%py3_install

# drop the tests, we do not need them in production, do not use rm -rf
pushd %{buildroot}%{python3_sitelib}
rm -f test/__pycache__/*
rmdir test/__pycache__
rm -f test/*
rmdir test
popd

# icon
install -Dpm 0644 icon_48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
desktop-file-install --add-category="Utility" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%check
%{python3} setup.py test

%files
%license LICENSE
%doc README.md
%{_bindir}/NanoVNASaver
%{python3_sitelib}/NanoVNASaver
%{python3_sitelib}/NanoVNASaver-%{version}-py*.egg-info
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-4
- Rebuilt for Python 3.9

* Tue Feb 25 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-3
- Fixed according to the review

* Fri Feb 21 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-2
- Fixed according to the review

* Wed Feb  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.2.2-1
- Initial version
