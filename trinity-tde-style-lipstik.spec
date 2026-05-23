%bcond clang 1

# TDE variables
%define tde_pkg tde-style-lipstik
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Lipstik style for TDE
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/themes/%{tarball_name}-%{version}.tar.xz

Obsoletes:		trinity-kde-style-lipstik < %{EVRD}
Provides:		trinity-kde-style-lipstik = %{EVRD}
Obsoletes:		trinity-style-lipstik < %{EVRD}
Provides:		trinity-style-lipstik = %{EVRD}

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Based on the plastik style, Lipstik is a purified style with many options to
tune your desktop look.

Lipstik also provides Lipstik-color-schemes


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/%{_lib}/trinity/tdestyle_lipstik_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_lipstik_config.so
%{tde_prefix}/%{_lib}/trinity/plugins/styles/lipstik.la
%{tde_prefix}/%{_lib}/trinity/plugins/styles/lipstik.so
%{tde_prefix}/share/apps/tdedisplay/color-schemes/lipstiknoble.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/lipstikstandard.kcsrc
%{tde_prefix}/share/apps/tdedisplay/color-schemes/lipstikwhite.kcsrc
%{tde_prefix}/share/apps/tdestyle/themes/lipstik.themerc

