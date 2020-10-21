%global extdir		%{_datadir}/gnome-shell/extensions/suspend-button@laserb
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global giturl		https://github.com/laserb/%{name}

%global commit		a81252074de99e2cdd29913b7f797a7f0d6d5b2b
%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%global commitdate	20171024
%global gitrel		.%{commitdate}git%{shortcommit}
%global gitver		-%{commitdate}git%{shortcommit}


Name:		gnome-shell-extension-suspend-button
Version:	19
Release:	7%{?gitrel}%{?dist}
Summary:	GNOME Shell Extension Suspend-Button by laserb

License:	GPLv2+
URL:		https://extensions.gnome.org/extension/826/suspend-button/
Source0:	%{giturl}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitversion}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	%{_bindir}/glib-compile-schemas

Requires:	gnome-shell-extension-common

%description
Allows to modify the suspend/shutdown button in the status menu.


%prep
%autosetup -n %{name}-%{commit} -p 1


%build
%make_build


%install
%make_install

# Cleanup crap.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install schema.
%{__mkdir} -p %{buildroot}%{gschemadir}
%{__cp} -pr _build/schemas/*gschema.xml %{buildroot}%{gschemadir}

# Install i18n.
%{_bindir}/find _build -name '*.po' -print -delete
%{__cp} -pr _build/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name


# Fedora handles this using triggers.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
	%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi


%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-7.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-6.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-5.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-4.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-3.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-2.20171024gita812520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 19-1.20171024gita812520
- Initial import (rhbz#1520152)

* Fri Dec 01 2017 Björn Esser <besser82@fedoraproject.org> - 19-0.1.20171024gita812520
- Initial rpm release (rhbz#1520152)
