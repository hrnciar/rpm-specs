Name: lazpaint
%global prettyname LazPaint

Summary: Simple image editor
URL: https://lazpaint.github.io

# LazPaint itself is GPLv3
# BGRABitmap and BGRAControls libraries are modified LGPLv2 (allow static linking in closed-source programs)
# BGRAControls also borrows some Boost-licensed code
License: GPLv3 and LGPLv2 and Boost

Version: 7.1.5
Release: 1%{?dist}

%global bitmap_version   11.2.5
%global controls_version 7.0

%global github https://github.com/bgrabitmap
Source0: %{github}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source10: %{github}/bgrabitmap/archive/v%{bitmap_version}/bgrabitmap-%{bitmap_version}.tar.gz
Source20: %{github}/bgracontrols/archive/v%{controls_version}/bgracontrols-%{controls_version}.tar.gz

Source100: %{name}.appdata.xml

BuildRequires: desktop-file-utils
BuildRequires: file
BuildRequires: fpc
BuildRequires: fpc-srpm-macros
BuildRequires: gtk2-devel
BuildRequires: lazarus
BuildRequires: libappstream-glib

BuildRequires: %{_bindir}/dos2unix

Requires: hicolor-icon-theme

ExclusiveArch: %{fpc_arches}


%description
%{prettyname} is a simple image editor, like PaintBrush or Paint.Net,
written in Lazarus (Free Pascal), using the BGRABitmap library.

It supports a variety of file formats, including layered bitmaps
and even 3D files.

%{prettyname} also offers a command-line interface for using it from a terminal,
as well as a Python script system that allows the user
to write their own layer effects.


%prep
%setup -q
ln %{SOURCE100} lazpaint/release/%{name}.appdata.xml

# unpack BGRABitmap
ln %{SOURCE10} ./bitmap.tgz
tar xzf ./bitmap.tgz
rm ./bitmap.tgz

mv bgrabitmap-%{bitmap_version}/bgrabitmap  ./bgrabitmap
rm -rf bgrabitmap-%{bitmap_version}/

# unpack BGRAControls
ln %{SOURCE20} ./controls.tgz
tar xzf ./controls.tgz
rm ./controls.tgz

mv bgracontrols-%{controls_version}  ./bgracontrols
rm -rf bgracontrols-%{controls_version}/

# Apply patches.
# We do it only now, and not right after %%setup, since some patches affect bgrabitmap/bgracontrols, too.
# - - - nothing to apply currently - - - #

# Some of the .po files have DOS line endings. Fix those.
dos2unix lazpaint/release/bin/i18n/*.po


%global laz_packages  %{expand:
	bgrabitmap/bgrabitmappack.lpk
	bgracontrols/bgracontrols.lpk
	lazpaintcontrols/lazpaintcontrols.lpk
}

%global laz_projects  %{expand:
	%{laz_packages}
	lazpaint/lazpaint.lpi
}

# Patch the project configuration files to enable debuginfo generation
LAZ_PROJECTS=(%{laz_projects})
for PROJECT in ${LAZ_PROJECTS[@]}; do
        sed  \
                -e 's|<GenerateDebugInfo Value="False"[ ]*/>|<GenerateDebugInfo Value="True"/>\n\t\t\t<DebugInfoType Value="dsDwarf2"/>|g'  \
		-e 's|<StripSymbols Value="True"[ ]*/>|<StripSymbols Value="False"/>|g'  \
                -i "${PROJECT}"
done


%build
LAZ_PACKAGES=(%{laz_packages})
LAZ_PROJECTS=(%{laz_projects})

# Inform lazbuild where to look for dependencies
for PACKAGE in ${LAZ_PACKAGES[@]}; do
	lazbuild --add-package-link "${PACKAGE}"
done

# lazbuild has a "--recursive" option for automatically compiling dependencies,
# but using this option triggers random crashes during the build.
# See: - https://bugs.freepascal.org/view.php?id=36318
#      - https://bugs.freepascal.org/view.php?id=36959
#
# As a workaround, we build everything manually in order.
for PROJECT in ${LAZ_PROJECTS[@]}; do
	lazbuild --build-mode=Release --widgetset=gtk2 --skip-dependencies "${PROJECT}"
done


# We need to manually compile the translation files
for PO_FILE in lazpaint/release/bin/i18n/*.po; do
	MO_FILE="$(dirname "${PO_FILE}")/$(basename "${PO_FILE}" ".po").mo"
	msgfmt --check -o "${MO_FILE}" "${PO_FILE}"
done

# Upstream provides a desktop file, but it's a bit of a mess
# and doesn't pass desktop-file-validate.
# Instead of trying to fix it, let's just write a desktop file ourselves.
cat > lazpaint/release/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{prettyname}
GenericName=Image editor
Comment=%{summary}
Icon=%{name}
Exec=%{_bindir}/%{name}
Terminal=false
Categories=Graphics
EOF


%install
# -- executable
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 lazpaint/release/bin/%{name} %{buildroot}%{_bindir}/

# -- run-time resources

RESDIR="%{buildroot}%{_datadir}/%{name}"
install -m 755 -d "${RESDIR}"
cp -a lazpaint/release/bin/models/ "${RESDIR}/models"

cp -a resources/scripts/ "${RESDIR}/scripts"
rm -rf "${RESDIR}/scripts/test/"

# -- translation files

for MO_SRC in lazpaint/release/bin/i18n/*.mo; do
	MO_FILE="$(basename "${MO_SRC}")"

	# The translation files have names like lazpaint.nl.mo
	# MO_TYPE - detect the translation type (lazpaint / lclstrconsts / lcresourcestring)
	MO_TYPE="$(echo "${MO_FILE}" | sed -e 's|\([^.]*\)\..*$|\1|')"
	# MO_LANG - detect the translation language
	MO_LANG="$(echo "${MO_FILE}" | sed -e 's|^[^.]*\.\([^.]*\)\.po$|\1|')"
	# English translation files do not have names ending in .en.mo, just .mo
	if [[ "${MO_LANG}" == "${MO_FILE}" ]]; then
		MO_LANG="en"
	fi

	MO_DIR="%{buildroot}%{_datadir}/locale/${MO_LANG}/LC_MESSAGES"
	install -m 755 -d "${MO_DIR}"
	install -m 644 -p "${MO_SRC}" "${MO_DIR}/${MO_TYPE}.mo"
done

%find_lang lazpaint
%find_lang lclstrconsts
%find_lang lcresourcestring


# -- 48px icon

PIXMAP_SOURCE="lazpaint/release/debian/pixmaps/lazpaint.png"
PIXMAP_SIZE="$(file "${PIXMAP_SOURCE}" | grep --only-matching -E -e '[0-9]+ x [0-9]+' | cut -f1 -d' ')"
PIXMAP_DIR="%{buildroot}%{_datadir}/icons/hicolor/${PIXMAP_SIZE}x${PIXMAP_SIZE}/apps"
install -m 755 -d "${PIXMAP_DIR}"
install -m 644 -p "${PIXMAP_SOURCE}" "${PIXMAP_DIR}/%{name}.png"

# -- hi-res icons

for ICON_SIZE in 512 1024; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 -p "resources/icon/lazpaint_icon_rendered_${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done

# -- desktop file and appstream data

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 -p lazpaint/release/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p lazpaint/release/%{name}.appdata.xml %{buildroot}%{_metainfodir}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files -f lazpaint.lang -f lclstrconsts.lang -f lcresourcestring.lang
%license COPYING.txt
%license bgracontrols/docs/COPYING.LGPL.txt
%license bgracontrols/docs/COPYING.modifiedLGPL.txt
%license "bgracontrols/docs/Boost Software License.txt"
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/**/apps/%{name}.png
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Mon Oct 19 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.5-1
- Update to v7.1.5 (with BGRABitmap v11.2.5 and BGRAControls v7.0)
- Update upstream URL
- Drop Patch0 (mangled headers in .po files - accepted upstream)
- Drop dependency on iconv (file encoding issues fixed upstream)

* Wed Oct 07 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 7.1.4-1
- Update to v7.1.4 (with BGRABitmap v11.2.4 and BGRAControls v6.9)
- Drop Patch0 (BGRABitmap conditional compilation failure - issue fixed upstream)
- Include models in the package
- Include translations in the package

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.3-3
- Add a patch to fix build failures with Lazarus 2.0.10

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.3-1
- Update to v7.1.3 (with BGRABitmap v11 and BGRAControls v6.7.1)
- Fix the Comment field in the auto-generated .desktop file
- Add an .appdata.xml file
- Preserve timestamps on icons

* Wed Apr 29 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.2-1
- Update to v7.1.2 (with BGRABitmap v10.9 and BGRAControls v6.6.1)
- Include lazpaint scripts in the package
- Install hi-res icons from the resources/icon/ directory
- Create a desktop entry file during build instead of using the upstream one

* Sun Apr 19 2020 Artur Iwicki <fedora@svgames.pl> - 7.1.1-1
- Initial packaging
