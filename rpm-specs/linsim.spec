Name:           linsim
Version:        2.0.3
Release:        6%{?dist}
Summary:        Tool for Amateur Radio Digital Mode evaluation

License:        GPLv3+
URL:            http://www.w1hkj.com
Source0:        http://www.w1hkj.com/files/test_suite/%{name}-%{version}.tar.gz
Source99:       linsim.appdata.xml

Patch0:         linsim-desktop.patch

# Utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
# Build dependencies
BuildRequires:  fltk-devel >= 1.3.4
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libpng-devel
BuildRequires:  libXft-devel


%description
Linsim is designed to read and then add path simulation to any monophonic wav
file recorded at any sampling rate. It works particularly well with files that
were created using fldigi’s audio capture and audio generate functions. The
entire wav file will be saved to computer memory and then duplicated during the
signal processing. The user should try to keep the length of the wav file at 20
Mg or less, but the author has tested some 200 Mg files on both Linux and
Windows-8 without causing a program fault. These files were original VOAR
broadcasts of about 30 minutes duration. The objective of this type of
simulation is to finally measure the character error rate (CER) and bit error
rate (BER) of a specific modem type and decoder design. For most modems a
sequence of 1000 characters provides a sufficient level of confidence in the
CER measurment.


%prep
%autosetup -p1


%build
# Work around fltk-devel bug in RHEL 7.
# https://bugzilla.redhat.com/show_bug.cgi?id=1510482
export LIBS="-lfltk"
%configure
%make_build


%install
%make_install

%if 0%{?fedora}
# Install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
install -pm 0644 %{SOURCE99} %{buildroot}%{_datadir}/metainfo/
%endif


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{?fedora:%{_datadir}/metainfo/%{name}.appdata.xml}
%{_datadir}/pixmaps/%{name}.xpm



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Initial packaging.
