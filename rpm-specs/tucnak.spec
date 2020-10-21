Name:		tucnak
Version:	4.20
Release:	4%{?dist}
Summary:	VHF contest logging program
License:	GPLv2
URL:		http://tucnak.nagano.cz/
Source0:	http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	libzia-devel = %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	fftw-devel
BuildRequires:	hamlib-devel
BuildRequires:	rtl-sdr-devel
BuildRequires:	libsndfile-devel
BuildRequires:	portaudio-devel
# For fixing files encoding
BuildRequires:	recode
Provides:	tucnak2 = %{version}-%{release}
Obsoletes:	tucnak2 < 2.31-21
# This is to rename soundwrapper from the generic name to the
# tucnak-soundwrapper, it can avoid name conflicts with other
# soundwrappers possibly shipped by other packages in the future.
Patch0:		tucnak-4.18-soundwrapper.patch
# Patch sent upstream
Patch1:		tucnak-4.20-fedora-fixes.patch

%description
Tucnak is VHF/UHF/SHF log for hamradio contests. It supports multi
bands, free input, networking, voice and CW keyer, WWL database and
much more.

%prep
%setup -q
%patch0 -p1 -b .soundwrapper
%patch1 -p1 -b .fedora-fixes

# fix encoding to UTF-8
recode ISO-8859-2..UTF-8 AUTHORS ChangeLog

%build
autoreconf -fi
%configure

%make_build

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# rename soundwrapper to tucnak-soundwrapper
mv %{buildroot}%{_bindir}/soundwrapper %{buildroot}%{_bindir}/tucnak-soundwrapper 

# drop docs installed to wrong place
rm -f %{buildroot}%{_datadir}/tucnak/doc/*
rmdir %{buildroot}%{_datadir}/tucnak/doc

# drop unneeded files/dirs
rm -f %{buildroot}%{_prefix}/lib/tucnak/tucnak.d
rmdir %{buildroot}%{_prefix}/lib/tucnak

%files
%license COPYING
%doc AUTHORS ChangeLog TODO
%doc doc/NAVOD.pdf doc/NAVOD.sxw
%doc data/*.html data/*.png
%{_bindir}/tucnak
%{_bindir}/tucnak-soundwrapper
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 4.20-3
- Rebuild for hamlib 4.

* Thu Feb  6 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20-2
- Variuos fixes according to the review

* Wed Feb  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.20-1
- New version

* Tue Jan 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.19-1
- New version
- Fixed according to the review

* Fri Jan  3 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 4.18-1
- Initial version
